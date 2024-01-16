import pandas as pd

# Program 3

csv = pd.read_csv("Math_IA_Data.csv")

filtered_csv = csv.dropna(axis='columns', how='all')

filtered_csv.to_csv("empty_columns_removed.csv")

