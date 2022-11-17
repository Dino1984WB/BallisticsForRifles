#!/usr/bin/env python3

import matplotlib.pyplot as mpl
import rifleData as rd
import pandas as pd
import numpy as np
from tabulate import tabulate

def graph():
    #graph with matplotlib

    #new dataframe from getData() in rifleData.py
    dfMainR = rd.getData() #grab dataframe of ballistics data from rifleData.py
    fig = mpl.figure() #figure..?
    ax = mpl.axes() #axis declaration


    x = np.array([0, 750])
    ax.plot(x, dfMainR)

    mpl.show() #sets graph visible

graph()
