# 📩 Email → WhatsApp Notification System (Python + IMAP + WhatsApp Cloud API)

Automatically receive WhatsApp notifications whenever a new email arrives in your inbox.  
Built with **Python**, **IMAP**, and the **WhatsApp Cloud API**, with secure environment variables.

---

## 🚀 Features

- Reads **unread emails** using IMAP (Gmail supported)
- Sends WhatsApp notifications with:
  - Sender
  - Subject
  - Email snippet (first 200 chars)
- Uses **official WhatsApp Cloud API**
- Secure with `.env` (no hardcoded credentials)
- Works 24/7 via cron job or cloud deployment
- Lightweight and beginner-friendly

---

## 🐍 Python Requirements

This project requires **Python 3.10 or above**.

### ✅ Supported versions:
- Python 3.10  
- Python 3.11  
- Python 3.12

### 📥 If you don’t have Python installed:

Download from:

👉 https://www.python.org/downloads/

✔ During installation on Windows, **check: “Add Python to PATH”**

---

## 📁 Project Structure

```
mail-to-whatsapp/
│
├── README.md
├── .gitignore
├── .env                # DO NOT UPLOAD — contains secrets
├── requirements.txt
└── src/
    ├── main.py
    ├── read_mail.py
    └── whatsapp_sender.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/mail-to-whatsapp.git
cd mail-to-whatsapp
```

---

## 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Gmail IMAP Setup

### Enable IMAP

1. Open Gmail  
2. Go to Settings → **See all settings**  
3. Forwarding & POP/IMAP  
4. Enable **IMAP**

### Create Gmail App Password

1. Google Account → **Security**  
2. Enable **2-Step Verification**  
3. Go to **App Passwords**  
4. Select:
   - App: Mail  
   - Device: Other → “IMAP App”
5. Copy the 16-digit password

---

## 4️⃣ WhatsApp Cloud API Setup

From Meta Developer Dashboard:

Copy:

| Needed Value | Where It's From |
|--------------|------------------|
| **WHATSAPP_TOKEN** | Permanent Access Token |
| **WHATSAPP_PHONE_ID** | Phone Number ID |
| **MY_NUMBER** | Your WhatsApp number (e.g., 91XXXXXXXXXX) |

Test the API:

```bash
curl -X POST \
  https://graph.facebook.com/v20.0/YOUR_PHONE_ID/messages \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "messaging_product": "whatsapp",
    "to": "91XXXXXXXXXX",
    "type": "text",
    "text": { "body": "WhatsApp API test successful!" }
  }'
```

You should receive a WhatsApp message.

---

## 5️⃣ Run the Project

```bash
python src/main.py
```

If unread emails exist → you’ll receive WhatsApp alerts instantly.

---

# 🌐 Deployment — Make it Run 24/7

## OPTION A — **Linux Cron Job** (run every 1 minute)

```
crontab -e
```

Add:

```
* * * * * python3 /full/path/mail-to-whatsapp/src/main.py
```

---

## OPTION B — **Railway.app** (Recommended)

1. Go to https://railway.app  
2. New Project → Deploy from GitHub  
3. Add environment variables under **Settings → Variables**  
4. Start command:

```
python src/main.py
```

5. Add a **Cron Job** to run every minute

---

## OPTION C — **Render.com**

1. Create new Web Service  
2. Runtime: **Python 3**  
3. Start command:

```
python src/main.py
```

4. Add environment variables under **Environment**  
5. Add a Render **Cron Job** for periodic execution

---

## 🛡️ Security Notes

- `.env` is listed in `.gitignore` (safe)
- Never upload API tokens or app passwords
- If you accidentally push a secret:
  - Remove it immediately  
  - Regenerate a new token

---

## ✨ Future Upgrades (Optional)

- Email importance filtering  
- Logging into a database  
- Multi-user support  
- Telegram + WhatsApp notifications  
- Dashboard to monitor activity  
- Support for email attachments  

---

## 👨‍💻 Author

