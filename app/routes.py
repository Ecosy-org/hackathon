from app import app
import requests
from flask import render_template
import json
import os
TOKEN = os.environ['AQICN_TOKEN']
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', token=TOKEN)