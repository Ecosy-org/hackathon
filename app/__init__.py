from flask import Flask

app = Flask(__name__, template_folder="templates")
app.static_folder = 'static'

from app import routes