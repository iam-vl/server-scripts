from datetime import datetime, timedelta
from tools import generate_short_id

from dbconfig import get_db_conn

def create_url(original_url: str, user_id: int = None) -> tuple[str, str]:
    print(f"Got user id: {user_id}")
    short_id = generate_short_id()
    delete_token = generate_short_id(16)
    num_days = 90 if user_id else 45
    expires_at = datetime.now() + timedelta(days=num_days)
    conn = get_db_conn()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO urls (id, original, expires_at, delete_token, user_id) VALUES (%s, %s, %s, %s, %s)",
            (short_id, original_url, expires_at, delete_token, user_id)
        )
    conn.commit()
    return short_id, delete_token 

def delete_url(short_id: str, delete_token: str) -> bool:
    print(1)
    conn = get_db_conn()
    print(2)
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM urls WHERE ID = %s AND delete_token = %s",
            (short_id, delete_token)            
        )
    print(3)
    conn.commit()
    return cur.rowcount > 0 # True if deleted, False otherwise 


def get_user_urls(user_id: str) -> list[dict]:
    conn = get_db_conn()
    with conn.cursor() as cur: 
        cur.execute(
            """
            SELECT id, original, created_at, expires_at
            FROM urls 
            WHERE user_id = %s
            ORDER BY created_at DESC;
            """,
            (user_id,)
        )
        columns = [desc[0] for desc in cur.description] # Get col names 
        return [dict(zip(columns, rows)) for row in cur.fetchall()]

