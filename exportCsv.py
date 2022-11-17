#Export to csv with this program
import pandas as pd
import csv as c
import rifleData as rd

df = rd.getData()
df.to_csv('C:\DataAnalytics\FinalData.txt')
