#!/usr/bin/env python3

import csv
import pandas as pd

def getData():

    #begin pandas stuff
    #grab files, produce a dataframe rom the csv files

    #imports all, only rifles, and then only hangun's ballistics
    #import Ballistics.csv
    
    #input_file_ballistics = "C:\\DataAnalytics\\Ballistics.csv"
    #datasetAll = pd.read_csv(input_file_ballistics)
    #dfA = pd.DataFrame(datasetAll)
    
    #import rifleCarts.csv
    input_file_rifle = "C:\\DataAnalytics\\rifleCartscsv.csv"
    datasetRifle = pd.read_csv(input_file_rifle)
    dfR = pd.DataFrame(datasetRifle)
    #import handgunCarts.csv
    input_file_handgun = "C:\\DataAnalytics\\handgunCartscsv.csv"
    datasetHandgun = pd.read_csv(input_file_handgun)
    dfH = pd.DataFrame(datasetHandgun)


    #remove unneeded cloumns from dataframes
    cols = [0,1,2]
    #dfcA = dfA[dfA.columns[cols]]
    dfcR = dfR[dfR.columns[cols]]
    dfcH = dfH[dfH.columns[cols]]


    #converts values of dfc dataframe to float (likely from string or int)
    #dfcA.astype(float)
    dfcR.astype(float)
    dfcH.astype(float)

    #print the dataframe dfc
    #print(dfcA.to_string())
    print(dfcR.to_string())
    print(dfcH.to_string())

    #Delimiter thingy that devides the nonsorted and sorted dataframes
    print("----------------------------------------\n")
    print("Above is unsorted list, below sorted by bullet weight")
    print("-----------------------------------------\n")  
    

    #dfc is a dataframe that can contain mass in grains of projectiles
    
    dfcR.sort_values(dfcR.columns[1])
    dfcH.sort_values(dfcH.columns[1])
    
    print(dfcR.to_string())
    print(dfcH.to_string())

    
    #send dataframe into a csv file
    dfcR.to_csv('CleanedBallisticRifleData.csv')
    dfcH.to_csv('CleanedBallisticHandgunData.csv')

    #waits for user input to hold open window
    pauseForever = input("Press any key to Continue")

getData()

