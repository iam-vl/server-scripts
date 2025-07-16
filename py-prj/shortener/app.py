import os, psycopg2, string 
import creds
from flask import Flask, render_template 

import random
from datetime import datetime, timedelta
from psycopg2 import sql 
from flask import request 

from flask import redirect 



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
    if request.method == "POST":
        original_url = request.form.get('url')
        if not original_url:
            return "This form requires a correct URL", 400
        short_id = generate_short_id() 
        expiry_date = datetime.now() + timedelta(days=45)
        try: 
            conn = get_db_conn()
            with conn.cursor() as cur:
                cur.execute(
                    sql.SQL("INSERT INTO urls (id, original, expires_at) VALUES (%s, %s, %s)"),
                    (short_id, original_url, expiry_date)
                )
            conn.commit()
            new_url = f"{request.host_url}{short_id}"
            return render_template('index.html', short_url=new_url)
        except Exception as e:
            return f"Error: {e}", 500
    return render_template('index.html')

@app.route('/<short_id>')
def redirect_to_original(short_id):
    try:
        conn = get_db_conn()
        with conn.cursor() as cur: 
            cur.execute(
                sql.SQL("SELECT original FROM urls WHERE id = %s AND expires_at > NOW()"),
                (short_id, )
            )
            result = cur.fetchone()
            if not result: 
                return "Link expired or not found", 404
            return redirect(result[0], code=301)
    except Exception as e:
        return f"Erroe: {e}", 500



if __name__ == '__main__':
    app.run(debug=True)