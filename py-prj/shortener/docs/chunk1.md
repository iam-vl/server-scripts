# Development steps 

## Project chunk 1: Barebones URL Shortener

Goal: Anon users can create/share short links via a web form or API.

Steps:   
1. Prep: Create folders, create  / activate a venv, install the dependencies:  
```sh
pip install flask psycopg2-binary python-dotenv
```  
2. Set up the DB: create the db + `migrations.sql` + `CREATE TABLE urls` (`id`, `original_url`, `created_at`, `expires_at`) + run the migrations:    
```sh  
psql -U postgres -d pgr_shortener -f migrations.sql
```   
3. Create a Flask app (`app.py`):  
    3.1. Set up a basic Flask app.  
    3.2. Shorten the URL.  
    3.3. Provide a redirect for the original page.  

<details>
    <summary>How to set up a basic Flask app: </summary>
  
    ```python
    import os, psycopg2, string 
    import creds
    from flask import Flask, render_template 

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-default') 
    def get_db_conn():
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME', 'shortener'), 
            user=os.getenv('DB_USER', 'postgres'),
            password=os.getenv('DB_PASSWORD', creds.db_password),
            host=os.getenv('DB_HOST', 'localhost')
        )
        return conn
    def generate_short_id(length=6):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))  

    @app.route('/', methods=['GET', 'POST']) # Ne
    def home():
        if method == 'POST': 
            pass
        return render_template('index.html')

    if __name__ == '__main__':
        app.run(debug=True)
    ```
</details>

<details>
    <summary>Показать логику для `/`, `/<id>`: </summary>  

```py

import random
from datetime import datetime, timedelta
from psycopg2 import sql 
from flask import request 
from flask import redirect 

@app.route('/', methods=['GET', 'POST'])
def home():
    # Ксли метод POST: 
        # извлекаем оригинальный урл
        original_url = request.form.get("url")
        # Если некорректные данные, возврат ошибка 400 
        if not original_url: 
            return "The form requires a valid url", 400
        # Считаем short id, считаем expiry date 
        short_id = generate_short_id()
        expiry_date = datetime.now() + timedelta(days=45)
        # try основная бизнес логика:  
        try:
            # Получаем коннекшн 
            conn = get_db_conn()
            # прогоняем запрос через курсор (conn.cursor())
            with conn.cursor() as cur:
                cur.execute(
                    sql.SQL("INSERT INTO urls (id, original, expires_at) VALUES (%s, %s, %s)"),
                    (short_id, original_url, expires_at)
                )
            # Коммитим 
            conn.commit()
            # Формируем урл: хост + id
            new_url = f"{request.host_url}{short_id}"
            # Возвращаем темплейт с новой ссылкой 
            return render_template("index.html", short_url=new_url)
        # в случае исключений: ошибка 500 
        return f"Error: {e}", 500 
    # Если метод GET, возвращаем пустой шаблон
    return render_template("index.html")

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
        return f"Error: {e}", 500
```
</details>






