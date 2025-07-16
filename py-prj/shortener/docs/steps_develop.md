# Development steps 

## Project chunk 1: Barebones URL Shortener

Goal: Anon users can create/share short links via a web form or API.

> **INFO**  
> How to enter the Docker postgresql shell:  
> `docker exec -it postgres1 psql -U postgres`  
> How to create db s on Docker:  
> `docker exec -it postgres1 psql -U postgres -c "CREATE DATABASE pgr_shortener;"`  
> Ноw to run the migrations on Docker: 
> 1. Copy the migrations file into the container:  
> `docker cp migrations.sql postgres1:/migration.sql` 
> 2. Execute the migrations inside the container: 
> `docker exec -it psql -U postgres -d pgr_shortener -f /migrations.sql`

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
    <summary>Показать логику для `/`: </summary>  

```py
@app.route('/', methods=['GET', 'POST'])
def home():
    # Ксли метод POST: 
        # извлекаем оригинальный урл
        # Если некорректные данные, возврат ошибка 400 
        # Считаем short id, считаем expiry date 
        # try основная бизнес логика:  
        try:
            # Получаем коннекшн 
            # прогоняем запрос через курсор (conn.cursor())
            with conn.cursor() as cur:
                cur.execute(
                    sql.SQL("INSERT INTO urls (id, original, expires_at) VALUES (%s, %s, %s)"),
                    (short_id, original_url, expires_at)
                )
            # Коммитим 
            # Формируем урл: хост + id
            # Возвращаем темплейт с новой ссылкой 
        # в случае исключений: ошибка 500 
    # Если метод GET, возвращаем пустой шаблон
```
</details>




## Project chunk 2:

Goal:   

Steps:   
1.  
2. 


## Project chunk 3:

Goal:   

Steps:   
1.  
2. 


## Project chunk 4:

Goal:   

Steps:   
1.  
2. 


