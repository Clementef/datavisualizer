from app.routes import app
from flask import render_template, redirect, request
from .Forms import MainForm
import requests
from .misc import graph

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MainForm(request.form)

    if request.method == "POST" and form.validate():

        graph(form.xData.data)


    return render_template('index.html', form=form)
