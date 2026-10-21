# Tabarak X - Subdomain Takeover Scanner

**Tabarak X** is an advanced, lightweight, and multi-threaded open-source reconnaissance and security scanner developed in Python. It is designed to help security researchers and developers identify potential **Subdomain Takeover** vulnerabilities quickly and efficiently by analyzing DNS CNAME records and matching them against known cloud service provider fingerprints.

---

## 🚀 Features

- **Real-time Reconnaissance:** Fetches live subdomains directly from Certificate Transparency logs (`crt.sh API`) with a robust fallback mechanism.
- **Accurate CNAME & Fingerprint Detection:** Uses system `nslookup` and HTTP/HTTPS requests to verify exact DNS responses and match them against known vulnerable cloud patterns (AWS, Azure, Heroku, GitHub Pages, Surge, etc.).
- **High Performance (Multithreading):** Utilizes `ThreadPoolExecutor` for concurrent scanning to achieve high speeds across large numbers of subdomains.
- **Automated Logging:** Automatically saves scan results with precise timestamps into a structured `results.txt` file.
- **Lightweight & Dependency-Friendly:** Built using standard Python libraries alongside the popular `requests` library.

---

## 🛠️ Prerequisites & Installation

Make sure you have Python 3 installed on your system. 

1. Clone the repository:
   ```bash
   git clone [https://github.com/engtabarak2026-hue/tabarak-scanner.git](https://github.com/engtabarak2026-hue/tabarak-scanner.git)
   cd tabarak-scanner
