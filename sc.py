import pandas as pd

# Read in csv files for each month
# store in a df
print ("starting read: ")
april_df = pd.read_csv("data/april_2024.csv")
print ("data/done with april")
may_df = pd.read_csv("data/may_2024.csv")
june_df = pd.read_csv("data/june_2024.csv", encoding = 'latin1') # latin 1 prevents read errors in june
july_df = pd.read_csv("data/july_2024.csv")
august_df = pd.read_csv("data/august_2024.csv")
september_df = pd.read_csv("data/september_2024.csv")
october_df = pd.read_csv("data/october_2024.csv")

# Combine all dfs into a single csv
combined_df = pd.concat([april_df, may_df, june_df, july_df, august_df, september_df, october_df], ignore_index= False)
combined_df.to_csv("combined_sheets_with_june.csv", index = False)