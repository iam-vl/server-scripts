from flask import Flask, request, jsonify
import smtplib 
from email.mime.text import MIMEText 
from dotenv import load_dotenv 
import os 

load_dotenv() # Load vars 
app = Flask(__name__)

@app.route("/send-email", methods = ["POST"])
def send_email():
    data = request.json 
    recipient = data.get("to")
    subj = data.get("subject")
    body = data.get("body") 

    # Email 
    msg = MIMEText(body)
    msg["Subject"] = subj 
    msg["From"] = os.getenv("OUTLOOK_EMAIL")
    msg["To"] = recipient 
    try: 
        # Conn to Outlook 
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
            server.starttls()
            server.login(os.getenv("OUTLOOK_EMAIL"), os.getenv("OUTLOOK_PASSWORD"))
            server.sendmail(os.getenv("OUTLOOK_EMAIL"), recipient, msg.as_string())
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5123)