from flask import Flask
from flask return render_template

app = Flask(__name__)

@app.route('/test123')
def test_page():
    return 'Hello! This is a static page. 🎉'



if __name__ == "__main__":
    app.run(debug=True)