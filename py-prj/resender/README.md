# Using resender 
 
```
pip unstall flask resend python-dotenv 
```

.env  
```  
OUTLOOK_EMAIL=you@outlook.com
OUTLOOK_PASSWORD=your_password_or_app_password
```  


```
curl -X POST http://127.0.0.1:5000/send-email \
  -H "Content-Type: application/json" \
  -d '{
    "to": "recipient@example.com",
    "subject": "Test from Flask + Outlook",
    "body": "This email was sent via Outlook SMTP!"
  }'
```