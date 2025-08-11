# Add email verification 

If flask-mail: `pip install flask-mail` 

Add to the migrations + run: 
```
ALTER TABLE users 
ADD COLUMN is_verified BOOLEAN DEFAULT FALSE,
ADD COLUMN verification_token TEXT
```

Add token generation funcs:  
```py
# Add to auth.py
from itsdangerous import URLSafeTimedSerializer

def generate_verification_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt='email-verify')

def verify_token(token, max_age=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt='email-verify',
            max_age=max_age
        )
    except:
        return None
    return email
```

Add to app.py: 
```py
import logging
from auth import generate_verification_token, verify_token

# Configure logging
logging.basicConfig(
    filename='email_simulator.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)
def mock_send_verification_email(email, verification_url):
    pass

# Updete registration route 

# Add verification endpoint 

```

