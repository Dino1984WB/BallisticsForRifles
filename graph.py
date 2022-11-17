import matplotlib.pyplot as mpl
import rifleData as rd
import pandas as pd
import numpy as np
from tabulate import tabulate

def graph():
    #graph with matplotlib

    dfMainR = rd.getData() #grab dataframe of ballistics data from rifleData.py
    fig = mpl.figure()
    ax = mpl.axes()

    x = np.linspace(6000, 30, 78)
    ax.plot(x, dfMainR)

    mpl.show() #sets graph visible

graph()
