#Author: William Bukowski

import csv as c
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

    #dfc is a dataframe that can contain mass in grains of projectiles
    R = dfcR.sort_values(dfcR.columns[0]) #sorts the Rifle records numerically
    H = dfcH.sort_values(dfcH.columns[0]) #sorts the Handgun records numerically
    
    #printThisR = 
    #printThisH = 
    #prints the dataframes to the console
    print(R.toString())
    #print(" ")
    #print(printThisH.to_string())

    #send dataframe into a csv file
    #dfcR.to_csv('CleanedBallisticRifleData.csv')
    #dfcH.to_csv('CleanedBallisticHandgunData.csv')

    #waits for user input to hold open window
    #pauseForever = input("Press any key to Continue")

    R.to_csv('C:\DataAnalytics\initData.txt') #from a no index .csv
    with open('C:\DataAnalytics\initData.txt') as infile, open('C:\DataAnalytics\FinalData.txt', 'w') as outfile:
        for idx, line in enumerate(infile):
            outfile.write(f'{idx},{line}')
    
    return R # add printThisH via comma later on


getData()

