import os, psycopg2, string 
import creds
from flask import Flask, render_template 

import random
from datetime import datetime, timedelta
from psycopg2 import sql 
from flask import request 

INSERT_URL_QUERY = "INSERT INTO urls (id, original, expires_at) VALUES (%s, %s, %s)"

app = Flask(__name__)
# See https://flask.palletsprojects.com/en/stable/config/#SECRET_KEY
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-default') 
def get_db_conn():
    print("Getting db conn....")
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME', 'pgr_shortener'), 
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', creds.db_password),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('PORT', '5431')
    )
    print(type(conn))
    return conn

def generate_short_id(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))  

@app.route('/', methods=['GET', 'POST'])
def home():
    # Ксли метод POST: 
    if request.method == 'POST':
        # извлекаем оригинальный урл
        # <input type="url" name="url"...>
        original_url = request.form.get('url')
        # Если некорректные данные, возврат ошибка 400 
        if not original_url: 
            return 'URL is required', 400 
        # Считаем short id, считаем expiry date 
        short_id = generate_short_id()
        # Anonymous expiry 
        expires_at = datetime.now() + timedelta(days=45) 

        try:
            print("Getting conn")
            conn = get_db_conn()
            print()
            with conn.cursor() as cur:
                print("trying to exec")
                q = f"INSERT INTO urls (id, original, expires_at) VALUES ({short_id}, {original_url}, {expires_at})"
                cur.execute(
                    sql.SQL("INSERT INTO urls (id, original, expires_at) VALUES (%s, %s, %s)"),
                    (short_id, original_url, expires_at)
                )
            print('before committing')
            conn.commit()
            short_url = f"{request.host_url}{short_id}"
            return render_template('index.html', short_url=short_url)
        except Exception as e:
            return f"Error: {e}", 500
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)