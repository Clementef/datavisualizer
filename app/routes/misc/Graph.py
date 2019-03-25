from .BarGraph import Bar
import pandas as pd
import os


def graph(xvalue):

    bar = Bar()

    cd = os.getcwd()
    data = pd.read_csv(cd.replace('\\', '/') + '/app/routes/misc/raw.csv')

    x = data[xvalue].unique()
    values = []

    for i in x:

        values.append(len(data[(data[xvalue] == i)]))

    bar.setaxis(x, values)

    bar.graph()
