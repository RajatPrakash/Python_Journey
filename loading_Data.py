import pandas as pd

data = pd.read_csv('pokemon_data.csv')
print(data)
print('\n')

# top 3 rows in data
print('Top three rows from data set')
print(data.head(3))
print('\n')

# bottom 3 rows
print('Bottom 3 rows only')
print(data.tail(3))

