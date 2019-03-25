from app.routes import app
from flask import render_template, redirect, request
from .Forms import MainForm
import requests

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MainForm(request.form)
    return render_template('index.html', form=form)
