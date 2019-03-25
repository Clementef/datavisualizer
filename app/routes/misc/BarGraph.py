import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Bar:

    def __init__(self):

        self.data = pd.read_csv("raw.csv")
        self.x = None
        self.y = None
        self.fig = Bar.figure(self)[0]
        self.ax = Bar.figure(self)[1]

    def figure(self):

        fig, ax = plt.plot()

        return fig, ax

    def graph(self):

        self.ax.bar(self.x, self.y)
