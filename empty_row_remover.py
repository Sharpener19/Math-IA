import pandas as pd
import csv

# Program 5

reader = pd.read_csv('RatingDiff_Result.csv')

filtered_reader = reader.dropna()

filtered_reader.to_csv('RD_R_Clear.csv')
