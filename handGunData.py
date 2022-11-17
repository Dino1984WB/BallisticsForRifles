import csv
import pandas as pd

def main():

    #grab file and turn its data into a dataframe with pandas
    input_file = "C:\\DataAnalytics\\Ballistics.csv"
    dataset = pd.read_csv(input_file)
    df = pd.DataFrame(dataset)

    #only grab the columns that we need
    cols = [3,4,5,6]
    dfc = df[df.columns[cols]]

    #convert the numbers in the df to floats
    dfc.astype(float) #this works!!! woohoo!!

    #print the dataframe out
    print(dfc.to_string())



main()
