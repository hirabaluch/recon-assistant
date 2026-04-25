# 🔎 Recon Assistant

<p align="center">
  <b>Automated Recon Tool for Subdomain & Endpoint Discovery</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue"/>
  <img src="https://img.shields.io/badge/Status-Active-success"/>
  <img src="https://img.shields.io/badge/License-MIT-green"/>
  <img src="https://img.shields.io/badge/Built%20for-Bug%20Bounty-red"/>
</p>

---

## 🚀 Overview

**Recon Assistant** is a fast and minimal CLI-based reconnaissance tool designed to automate the **initial recon phase** of penetration testing and bug bounty hunting.

It helps identify:

* Subdomains
* Hidden endpoints
* Live services

---

## ⚡ Features

* 🔍 Subdomain Enumeration
* 🌐 Endpoint Discovery
* 📡 HTTP Status Code Detection
* 💾 Automatic Output Saving
* ⚡ Lightweight & Fast Execution

---

## 🛠️ Installation

```bash
git clone https://github.com/hirabaluch/recon-assistant.git
cd recon-assistant

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## ⚙️ Usage

```bash
python main.py -d <domain>
```

### Example:

```bash
python main.py -d example.com
```

### Optional:

```bash
-w, --wordlist   Use custom wordlist
```

---

## 📸 Example Output

```
[*] Scanning subdomains...
[+] http://api.example.com [200]
[+] http://admin.example.com [200]

[*] Scanning endpoints...
[+] /login [200]
[+] /admin [403]

[*] Results saved in output/results.txt
```

---

## 📂 Output

Results are stored in:

```
output/results.txt
```

---

## 📁 Project Structure

```
recon-assistant/
├── core/
├── data/
├── output/
├── main.py
├── requirements.txt
└── README.md
```

---

## 🎯 Use Cases

* Bug bounty reconnaissance
* Attack surface mapping
* Initial penetration testing

---

## ⚠️ Disclaimer

This tool is for **educational and authorized use only**.
The author is not responsible for misuse.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Hira Baluch**

---

<p align="center">
⭐ Star this repository if you found it useful!
</p>
