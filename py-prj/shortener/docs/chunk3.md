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
 
```

