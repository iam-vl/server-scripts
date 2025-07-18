import os
from flask import Flask, render_template 

# import random
# from datetime import datetime, timedelta
from psycopg2 import sql 
from flask import request 

from flask import redirect 

# for the delete link - chunk 2
from urllib.parse import quote
import models


INSERT_URL_QUERY = "INSERT INTO urls (id, original, expires_at) VALUES (%s, %s, %s)"

app = Flask(__name__)
# See https://flask.palletsprojects.com/en/stable/config/#SECRET_KEY
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-default') 



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        original_url = request.form.get('url')
        short_id, delete_token = models.create_url(original_url)
        short_url = f"{request.host_url}{short_id}"
        delete_link = f"{request.host_url}delete/{short_id}/{quote(delete_token)}"
        return render_template('index.html', short_url=short_url, delete_link=delete_link)
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

@app.route("/delete/<short_id>/<token>")
def delete(short_id, token):
    if models.delete_url(short_id, token):
        return "Link deleted"
    return "Invalid token or id", 404

if __name__ == '__main__':
    app.run(debug=True)