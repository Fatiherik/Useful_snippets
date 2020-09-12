# pip3 install pandas
# pip3 install xlrd (required by pandas)

import pandas as pd

# YOU MUST PUT sheet_name=None TO READ ALL CSV FILES IN YOUR XLSM FILE
df = pd.read_csv('optRatios.csv')

# prints all sheets
print(df)

# prints all sheets name in an ordered dictionary
print(df.keys())

# prints first sheet name or any sheet if you know it's index
first_sheet_name = list(df.keys())[0]
print(first_sheet_name)

# prints first sheet or any sheet if know it's name
print(df[first_sheet_name])

# export first sheet to file
df['Sheet3'].to_csv('optRatios.csv')

# export all sheets
for sheet_name in list(df.keys()):
   df[sheet_name].to_csv(sheet_name + 'Sheet.csv')
