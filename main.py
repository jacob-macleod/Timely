from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from database.py import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

app.run(debug=True, host='0.0.0.0')