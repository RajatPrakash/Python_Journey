import pandas as pd

data = pd.read_csv('pokemon_data.csv')

# Read headers
print(data.columns)

# read Each column

print(data[['Name', 'Attack']][0:5])
print('\n')

# read each rows
print(data.iloc[1])  # iloc --> integer location based on index
print('\n')

# read from specific location (row,column)
print(data.iloc[2, 1])

# iterate through each row
for index, row in data.iterrows():
    print(index, row['Name'])
