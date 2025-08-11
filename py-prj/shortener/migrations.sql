CREATE TABLE urls (
    id CHAR(10) PRIMARY KEY,
    original TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    expires_at TIMESTAMPTZ
);
ALTER TABLE urls ADD COLUMN delete_token TEXT;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,  -- Store hashed passwords only!
  created_at TIMESTAMPTZ DEFAULT NOW()
);
-- Link urls to users
ALTER TABLE urls ADD COLUMN user_id INTEGER REFERENCES users(id);

-- Chunk 5: email verification
ALTER TABLE users 
ADD COLUMN is_verified BOOLEAN DEFAULT FALSE, 
ADD COLUMN verification_token TEXT;