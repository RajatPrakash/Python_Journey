import pandas as pd

data = pd.read_csv('modified_pokemon_data.csv')
print(data.columns)  # printing the columns headings

data.loc[data['Total'] > 500, ['Generation', 'Legendary']] = 'Wait for it'

# print(modified_data)
print(data)