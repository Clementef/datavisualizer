from app.routes import app
from flask import render_template, redirect


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')