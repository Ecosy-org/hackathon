from app import app
import os
TOKEN = os.environ['AQICN_TOKEN']
from flask import (Flask,
                   redirect,
                   url_for,
                   request,
                   render_template)

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html', token=TOKEN)

@app.route('/sources')
def sources():
    return render_template('sources.html')

@app.route('/about')
def about():
    return render_template('about.html')
