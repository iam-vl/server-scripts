import os
import psycopg2
import creds

def get_db_conn():
    print("Getting db conn....")
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME', 'pgr_shortener'), 
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', creds.db_password), # in .gitignore
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('PORT', '5431')
    )
    print(type(conn))
    return conn