
# app.py
from flask import Flask, render_template, request


app= Flask(__name__)
## __name__ is the application name


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/home')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True) 