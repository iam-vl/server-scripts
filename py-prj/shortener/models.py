def create_url(original_url: str) -> tuple[str, str]:
    short_id = generate_short_id()
    delete_token = generate_short_id(16)
    expires_at = datetime.now() + timedelta(days=45)
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO urls (id, original, expires_at, delete_token) VALUES (%s, %s, %s, %s)",
            (short_id, original_url, expires_at, delete_token)
        )
    conn.commit()
    return short_id, delete_token 

def delete_url(short_id: str, delete_token: str) -> bool:
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM urls WHERE ID = %s AND delete_token = %s",
            (short_id, delete_token)            
        )
    conn.commit()
    return cur.rowcount > 0 # True if deleted, False otherwise 
    