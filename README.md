# 🛡️ Nexus Header Auditor — Web HTTP Security Checker

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-000000?style=for-the-badge&logo=flask&logoColor=white)
![OWASP](https://img.shields.io/badge/OWASP-Security_Best_Practices-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Nexus Header Auditor** adalah aplikasi analisis keamanan web pasif (*defensive security tool*) berbasis Flask. Alat ini bertugas mengevaluasi konfigurasi *HTTP Response Headers* pada web server target berdasarkan panduan standar keamanan **OWASP (Open Web Application Security Project)**.

---

## ✨ Fitur Utama

- 🔍 **OWASP Header Inspection:** Menganalisis 6 *security header* utama (`HSTS`, `CSP`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, dan `Permissions-Policy`).
- 📊 **Automated Scoring & Grading:** Mengalkulasi tingkat keamanan web dari 0% hingga 100% dan mengelompokkannya ke dalam *Grade* A sampai F.
- 🎯 **Browser User-Agent Spoofing:** Dilengkapi *header requests* kustom yang menyerupai browser Chrome asli untuk melewati blokir bot dasar/WAF.
- 💡 **Vulnerability Context:** Menyediakan deskripsi risikonya (seperti ancaman XSS, Clickjacking, dan MITM) jika *header* keamanan absen.
- 🎨 **Modern Dark UI:** Tampilan antarmuka yang responsif, bersih, dan mudah dipahami.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.x, Flask, Requests
- **Frontend:** HTML5, CSS3, FontAwesome 6

---

## 🚀 Cara Menjalankan

1. **Kloning Repositori:**
   ```bash
   git clone [https://github.com/username-kamu/nexus-header-auditor.git](https://github.com/username-kamu/nexus-header-auditor.git)
   cd nexus-header-auditor
