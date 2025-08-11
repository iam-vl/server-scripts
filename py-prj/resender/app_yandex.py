import smtplib
from email.mime.text import MIMEText
from flask import Flask, request

app = Flask(__name__)

@app.route("/send-email", methods=["POST"])
def send_email():
    # Yandex SMTP Config
    smtp_server = "smtp.yandex.com"
    port = 465  # SSL (or 587 for TLS)
    sender_email = "v4ssily.la@yandex.ru"  # Must be Yandex domain
    password = "lqkdvspfwyteaynm"   # Generated in Yandex ID

    # Email content
    recipient = request.json.get("to")
    msg = MIMEText(request.json.get("body"))
    msg["Subject"] = request.json.get("subject")
    msg["From"] = sender_email
    msg["To"] = recipient

    try:
        with smtplib.SMTP_SSL(smtp_server, port) as server:  # Use SMTP_SSL for port 465
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient, msg.as_string())
        return "Email sent!"
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)