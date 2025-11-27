import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")

def decode_header_value(value):
    decoded, encoding = value
    if isinstance(decoded, bytes):
        return decoded.decode(encoding or "utf-8", errors="ignore")
    return decoded

def read_unread_emails():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, "UNSEEN")
    mail_ids = messages[0].split()

    unread = []

    for msg_id in mail_ids:
        _, msg_data = mail.fetch(msg_id, "(RFC822)")
        raw_msg = msg_data[0][1]
        msg = email.message_from_bytes(raw_msg)

        # Subject
        subject_header = decode_header(msg["Subject"])[0]
        subject = decode_header_value(subject_header) if subject_header else "No Subject"

        # From
        from_ = msg.get("From", "Unknown Sender")

        # Body snippet
        snippet = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    snippet = part.get_payload(decode=True).decode(errors="ignore")[:200]
                    break
        else:
            payload = msg.get_payload(decode=True)
            if payload:
                snippet = payload.decode(errors="ignore")[:200]

        unread.append({
            "subject": subject,
            "from": from_,
            "snippet": snippet
        })

    mail.logout()
    return unread
