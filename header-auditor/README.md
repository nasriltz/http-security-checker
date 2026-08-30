# 🛡️ Web HTTP Security Header Auditor

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-000000?style=for-the-badge&logo=flask&logoColor=white)
![OWASP](https://img.shields.io/badge/OWASP-Security_Best_Practices-orange?style=for-the-badge)

Aplikasi audit keamanan web berbasis **Flask** untuk menguji dan menganalisis keberadaan **HTTP Security Headers** pada web server sesuai dengan rekomendasi standar **OWASP (Open Web Application Security Project)**.

---

## ✨ Fitur Utama

- 🔍 **Automated Header Inspection:** Menganalisis 6 *security header* krusial (HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, dan Permissions-Policy).
- 📊 **Security Scoring System:** Menghitung skor persentase keamanan dan memberikan *Grade* (A - F) secara otomatis.
- 💡 **Severity & Vulnerability Context:** Memberikan deskripsi teknis mengenai potensi celah keamanan (XSS, Clickjacking, MIME-Sniffing) jika *header* tidak terpasang.
- 🎨 **Modern Dark UI:** Antarmuka responsif berbasis HTML5/CSS3.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.x, Flask, `requests`
- **Frontend:** HTML5, CSS3, FontAwesome 6

---

## 🚀 Cara Menjalankan

1. **Kloning Repositori:**
   ```bash
   git clone [https://github.com/nasriitz/header-auditor.git](https://github.com/nasriitz/header-auditor.git)
   cd header-auditor