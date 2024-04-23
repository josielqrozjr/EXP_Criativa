# app.py

from flask import Flask, render_template

app= Flask(__name__)
## __name__ is the application name

@app.route('/')
def index():
    return render_template("/templates/index.html")

@app.route('/sensors')
def sensors():
    return render_template("sensors.html")
