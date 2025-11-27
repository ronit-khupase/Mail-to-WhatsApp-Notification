from read_mail import read_unread_emails
from whatsapp_sender import send_whatsapp_message

def run():
    emails = read_unread_emails()

    if not emails:
        print("No new emails.")
        return

    for mail in emails:
        msg = f"""
📩 *New Email Received!*

From: {mail['from']}
Subject: {mail['subject']}

Snippet:
{mail['snippet']}
        """
        send_whatsapp_message(msg)
        print("WhatsApp notification sent!")

if __name__ == "__main__":
    run()
