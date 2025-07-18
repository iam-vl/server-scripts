CREATE TABLE urls (
    id CHAR(10) PRIMARY KEY,
    original TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    expires_at TIMESTAMPTZ
);
ALTER TABLE urls ADD COLUMN delete_token TEXT;