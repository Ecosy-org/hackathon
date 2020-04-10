from app import app

from flask import (Flask,
                   redirect,
                   url_for,
                   request,
                   render_template)

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

