#!/usr/bin/env python3

import csv
import pandas as pd

def getData():

    #begin pandas stuff
    #grab files, produce a dataframe rom the csv files 
    
    #import rifleCarts.csv
    input_file_rifle = "C:\\DataAnalytics\\rifleCartscsv.csv"
    datasetRifle = pd.read_csv(input_file_rifle)
    dfR = pd.DataFrame(datasetRifle)
    #import handgunCarts.csv
    input_file_handgun = "C:\\DataAnalytics\\handgunCartscsv.csv"
    datasetHandgun = pd.read_csv(input_file_handgun)
    dfH = pd.DataFrame(datasetHandgun)

    #remove unneeded columns from the two dataframes
    cols = [0,1,2] #selects columns with array counting
    dfcR = dfR[dfR.columns[cols]] #selects specific columns for Rifle
    dfcH = dfH[dfH.columns[cols]] #selects specific columns for Handgun

    #converts values of dfc dataframe to float (likely from string or int)
    #dfcA.astype(float)
    dfcR.astype(float)
    dfcH.astype(float)

    #print the dataframe dfc
    #print(dfcA.to_string())
    #print(dfcR.to_string())
    #print(dfcH.to_string())

    #Delimiter thingy that devides the nonsorted and sorted dataframes
    print("\n\n\n\n")
    print("Below is the data sorted by bullet weight:")
    print("\n\n\n\n\n")

    #dfc is a dataframe that can contain mass in grains of projectiles
    printThisR = dfcR.sort_values(dfcR.columns[0]) #sorts the Rifle records numerically
    printThisH = dfcH.sort_values(dfcH.columns[0]) #sorts the Handgun records numerically
    
    #prints the dataframes to the console
    print(printThisR.to_string())
    print("^Rifle data, above | below, Handgun data")
    print(printThisH.to_string())

    #send dataframe into a csv file
    #dfcR.to_csv('CleanedBallisticRifleData.csv')
    #dfcH.to_csv('CleanedBallisticHandgunData.csv')

    #waits for user input to hold open window
    pauseForever = input("Press any key to Continue")



getData()

