# Chunk 3: Email + Password Auth 

## Update the dependencies + db schema  
Install dependencies:   
```sh 
pip install flask-login werkzeug  # For auth and password hashing
```
Update the db schema: 
```sql  
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,  -- Store hashed passwords only!
  created_at TIMESTAMPTZ DEFAULT NOW()
);
-- Link urls to users
ALTER TABLE urls ADD COLUMN user_id INTEGER REFERENCES users(id);
```

## Set up the auth 

Create `auth.py`:  
```py 
from flask_login import LoginManager, UserMixin 
from werkzeug.security import generate_password_hash, check_password_hash 
from dbconfig import get_db_conn 

login_manager = LoginManager() 
class User(UserMixin):
    def __init__(self, id, email):
        self.id = id
        self.email = email 

@login_manager.user_loader 
def load_user(user_id: str) -> User: 
    print("Loading user...")
    conn = get_db_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT id, email FROM users WHERE user_id = %s", (user_id,))
        user_data = cur.fetchone()
        return User(*user_data) if user_data else None

def create_user(email: str, password: str) -> User:
    conn = get_db_conn()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO users (email, password_hash) VALUES(%s, %s) RETURNING id",
            (email, generate_password_hash(password))
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
```

## Add routes  

```py

# Adding email login/ logout routes 
from flask_login import login_user, logout_user, login_required, current_user 
from auth import create_user, verify_user, login_manager 

# Init app

# Init login manager 
login_manager.init_app(app)
login_manager.login_view = 'login' 

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = create_user(email, password)
        login_user(user)
        return redirect('/')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = verify_user(email, password)
        if user:
            login_user(user)
            return redirect('/')
        return "Invalid credentials", 401
    return render_template('login.html')

@app.route('logout')
def logout():
    logout_user()
    return redirect('/')
```

## Add templates 

Add templates: `register.html`, `login.html`. Example: 

```html

<form method="POST">
  <input type="email" name="email" placeholder="Email" required>
  <input type="password" name="password" placeholder="Password" required>
  <button type="submit">Login</button>
</form>

```

## Link URLs with users 

Update `models.py`: 
```py
def create_url(original_url: str) -> tuple[str, str]:
    short_id = generate_short_id()
    delete_token = generate_short_id(16)
    num_days = 90 if user_id else 45
    expires_at = datetime.now() + timedelta(days=num_days)
    conn = get_db_conn()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO urls (id, original, expires_at, delete_token) VALUES (%s, %s, %s, %s)",
            (short_id, original_url, expires_at, delete_token)
        )
    conn.commit()
    return short_id, delete_token 
```

## Test: 

`/register` -> Create account -> Shorten a URL -> Check the db 