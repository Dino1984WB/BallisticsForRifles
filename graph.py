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
    
    print(dfMainR.toString())
    #create datasets for x, y axis
    x = dfMainR["Weight"]
    y = dfMainR["V0"]
    y2 = dfMainR["V100"]

    pd.reset_index()

    fig = mpl.figure() #figure..?
    ax = mpl.axes() #axis declaration

    #graph declaration
    ax.plot() #plot the np array against the dfMainR dataframe

    #test: determine contents of dfMainR
    print(dfMainR.to_string())    


    mpl.show() #sets graph visible

graph()
