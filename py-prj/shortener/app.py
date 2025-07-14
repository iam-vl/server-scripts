import os, psycopg2, string 
import creds
from flask import Flask, render_template 

app = Flask(__name__)
# See https://flask.palletsprojects.com/en/stable/config/#SECRET_KEY
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

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)