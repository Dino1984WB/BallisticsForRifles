#!/usr/bin/env python3

import csv
import pandas as pd

def main():
    #Data derivation done here ->

    #begin pandas stuff
    #grab files, produce a dataframe rom the csv files


    #import Ballistics.csv
    input_file_ballistics = "C:\\DataAnalytics\\Ballistics.csv"
    datasetAll = pd.read_csv(input_file_ballistics)
    df = pd.DataFrame(dataset)

    #import rifleCarts.csv
    input_file_rifle = "C:\\DataAnalytics\\rifleCarts.csv"
    datasetRifle = pd.read_csv(input_file_rifle)
    df = pd.DataFrame(dataset)

    #import handgunCarts.csv
    input_file_handgun = "C:\\DataAnalytics\\handgunCarts.csv"
    datasetHandgun = pd.read_csv(input_file_handgun)
    df = pd.DataFrame(dataset)

    #remove unneeded cloumns from dataframe df - > dfc
    cols = [2,3,4,5,6]
    dfc = df[df.columns[cols]]

    #converts values of dfc dataframe to float (likely from string or int)
    dfc.astype(float)

    #print the dataframe dfc
    print(dfc.to_string())

    #Delimiter thingy
    print("----------------------------------------\n")
    print("Above is unsorted list, below sorted by bullet weight")
    print("-----------------------------------------\n")  

    #dfc is a dataframe that can contain mass in grains of projectiles
    #1000 > n > 0, but range is practically speaking smaller
    #cut off at/including row 75
    dfg = dfc.sort_values("Weight")
    print(dfg.to_string())

    #send dataframe into a csv file
    dfg.to_csv('CleanedBallisticsData.csv')

    #waits for user input to hold open window
    pauseForever = input("Press any key to Continue")

main()
