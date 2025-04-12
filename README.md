

# 📧 EMAIL ANALYZER | Advanced Email Security Tool 🔐  



**Developer:** [Anupam Pal ]     🌐 LinkedIn Profile:-   (https://linkedin.com/in/anupam-pal-58246025a) |

---

## 🧠 Project Overview

**Email Analyzer** is a full-stack web application built with **Python Django** to analyze `.eml` email files and domain-related DNS records. It helps detect **email spoofing**, **phishing**, and **malicious links or attachments**, improving your **cybersecurity posture**.

This tool empowers security analysts and users to inspect the inner workings of emails, detect forgery, and verify sender authenticity via SPF, DKIM, and DMARC protocols.

---

## 🚀 Features at a Glance

✨ A snapshot of what this tool can do for you:

- 📬 **Email Parser**
  - Upload `.eml` files to extract sender, recipient, subject, and routing path
  - Analyze received headers to understand email flow

- 🔍 **Spoof Detection**
  - Check if an email passes SPF, DKIM, and DMARC validation
  - Detect forged sender identities (anti-spoof)

- 🌐 **DNS Record Checker**
  - Retrieve and display domain records:
    - `A`, `MX`, `NS`, `CNAME`, `TXT`, `SPF`, `DKIM`, `DMARC`

- 🧪 **VirusTotal Integration**
  - Scan email attachments and URLs using VirusTotal API
  - Identify malware, phishing links, and threats

- 🌗 **Modern UI**
  - Fully responsive frontend with:
    - Light/Dark mode toggle
    - Email animation effects
    - Clean dashboard
    - PDF export feature


---

## ⚙️ How to Use

### 📩 1. Analyze Emails
- Navigate to the **Email Analyzer** section
- Upload your `.eml` file
- Click **"Analyze"** to get a detailed report

### 🌍 2. Check DNS & Spoofing
- Go to the **Domain Analyzer** section
- Enter your domain name
- Click **"Check Domain"** to get DNS, SPF, DKIM, DMARC info

---

## 📂 Project Folder Structure


---

## 🛠️ Installation Instructions

```bash
# 1. Clone the repository
git clone https://github.com/anupampal01/email-analyzer.git
cd email-analyzer

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the development server
python manage.py runserver

# 6. Visit in your browser
http://127.0.0.1:8000/




Hi, I’m Anupam Pal – a passionate full-stack developer and cybersecurity enthusiast. I love building tools that help others stay safe and productive online.



💡 I welcome collaboration, feedback, and contribution. Let’s build something secure together!