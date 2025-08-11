## Microb 



```
microb/
  venv/
  app/
    __init__.py
    routes.py
  microb.py
```

Init:  
```py 
from flask import Flask
app = Flask(__name__)
from app import routes
```  
Routes:  
```py 
from app import app
@app.route("/")
@app.route("/index")
def index(): return "HW"
```

Microb: `from app import app`


```sh
export FLASK_APP=microb.py
# windows
# set FLASK_APP=microb.py
```

```sh
flask run 
flask run --port 5001
```  

To remember the env variables:
```sh
pip install python-dotenv
touch .flaskenv
```
Flaskenv:  `FLASK_APP=microb.py` 

## CH02 Templates 

Create /app/templates/index.html
```
    <head>
        <title>{{ title }} - Microblog</title>
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
    </body>
```

