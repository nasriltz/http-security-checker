from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Daftar Security Header Standar OWASP & Penjelasannya
SECURITY_HEADERS = {
    "Strict-Transport-Security": {
        "desc": "Memaksa koneksi aman menggunakan HTTPS (Mencegah Man-in-the-Middle Attack).",
        "severity": "High"
    },
    "Content-Security-Policy": {
        "desc": "Membatasi sumber resource yang boleh dimuat (Mencegah XSS & Data Injection).",
        "severity": "High"
    },
    "X-Frame-Options": {
        "desc": "Mencegah situs dimuat dalam <iframe> di situs lain (Mencegah Clickjacking).",
        "severity": "Medium"
    },
    "X-Content-Type-Options": {
        "desc": "Mencegah browser menebak tipe MIME file (Mencegah MIME-sniffing exploits).",
        "severity": "Medium"
    },
    "Referrer-Policy": {
        "desc": "Mengatur informasi referer URL yang dikirim saat mengklik link keluar.",
        "severity": "Low"
    },
    "Permissions-Policy": {
        "desc": "Membatasi akses situs ke fitur browser seperti kamera, mikrofon, atau lokasi.",
        "severity": "Low"
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    audit_results = None
    target_url = ""
    score = 0
    grade = "F"
    error_msg = None

    if request.method == "POST":
        target_url = request.form.get("target_url", "").strip()
        
        # Validasi skema URL
        if not target_url.startswith(("http://", "https://")):
            target_url = "https://" + target_url

        try:
            # Kirim HTTP Request ke URL target
            response = requests.get(target_url, timeout=7, headers={"User-Agent": "Nexus-Header-Auditor/1.0"})
            response_headers = response.headers

            audit_results = []
            passed_count = 0

            for header_name, info in SECURITY_HEADERS.items():
                is_present = header_name in response_headers
                if is_present:
                    passed_count += 1
                
                audit_results.append({
                    "name": header_name,
                    "status": is_present,
                    "value": response_headers.get(header_name, "Tidak Ditemukan"),
                    "desc": info["desc"],
                    "severity": info["severity"]
                })

            # Hitung Skor & Grade (0 - 100%)
            total_headers = len(SECURITY_HEADERS)
            score = round((passed_count / total_headers) * 100)

            if score >= 85: grade = "A"
            elif score >= 70: grade = "B"
            elif score >= 50: grade = "C"
            elif score >= 30: grade = "D"
            else: grade = "F"

        except requests.exceptions.RequestException as e:
            error_msg = f"Gagal menghubungkan ke target ({target_url}). Pastikan URL valid dan server aktif."

    return render_template(
        "index.html", 
        results=audit_results, 
        target=target_url, 
        score=score, 
        grade=grade, 
        error=error_msg
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)