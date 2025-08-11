from flask_login import LoginManager, UserMixin 
from werkzeug.security import generate_password_hash, check_password_hash 
from dbconfig import get_db_conn 

# Add token generation 
from itsdangerous import URLSafeTimedSerializer

login_manager = LoginManager() 

class User(UserMixin):
    def __init__(self, id, email):
        self.id = id
        self.email = email 

@login_manager.user_loader 
def load_user(user_id):
    print("Loading user...")
    conn = get_db_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT id, email FROM users WHERE id = %s", (user_id,))
        user_data = cur.fetchone()
        print(f"User data: {user_data}\t Type: {type(user_data)}")
        return User(*user_data) if user_data else None

def create_user(email: str, password: str) -> User:
    conn = get_db_conn()
    with conn.cursor() as cur:
        verification_token = generate_verification_token(email) # Generate toekn
        cur.execute(
            "INSERT INTO users (email, password_hash, verification_token) VALUES(%s, %s, %s) RETURNING id",
            (email, generate_password_hash(password), verification_token)
        )
        user_id = cur.fetchone()[0]
        conn.commit()
    return User(user_id, email)

def verify_user(email: str, password: str) -> User | None:
    conn = get_db_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT id, password_hash FROM users WHERE email=%s", (email,))
        userdata = cur.fetchone()
        if userdata and check_password_hash(userdata[1], password):
            return User(userdata[0], email)
    return None


def generate_verification_token(email: str): 
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt='email-verify')
def verify_token(token, max_age=3600) -> str:
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token, 
            salt = 'email-verify',
            max_age = max_age
        )
    except:
        return None
    return email

