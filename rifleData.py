#!/usr/bin/env python3

import csv
import pandas as pd

def main():
    
    #begin pandas stuff
    #grab file, produce a dataframe of certain columns only
    input_file = "C:\\DataAnalytics\\Ballistics.csv"
    dataset = pd.read_csv(input_file)
    df = pd.DataFrame(dataset)

    cols = [2,3,4,5,6]
    dfc = df[df.columns[cols]]

    dfc.astype(float) #this works!!! woohoo!!

    print(dfc.to_string())
    print("----------------------------------------\n")
    print("Above is unsorted list, below sorted by bullet weight")
    print("-----------------------------------------\n")


    #dfc is a dataframe that can contain mass in grains of projectiles
    #1000 > n > 0, but range is practically speaking smaller
    #cut off at/including row 75
    dfg = dfc.sort_values("Weight")
    print(dfg.to_string())

    dfg.to_csv('CleanedBallisticsData.csv')

    pauseForever = input("Press any key to Continue")

main()
