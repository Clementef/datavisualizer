from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

import pandas as pd
import os
def getDataOptions():
    cd = os.getcwd()
    table = pd.read_csv(cd.replace('\\','/')+'/app/routes/misc/raw.csv')
    colNames = []
    for i in table:
        colNames.append("i")
    data = list(zip(colNames, colNames))
    return data

class GiveForm(FLaskForm):
    dataOptions = selectField("Data Options", choices=getDataOptions())
    graphOptions = selectField("Graph Options",
    choices=[("Bar Graph", "Bar Graph"), ("Pie Chart", "Pie Chart")])
