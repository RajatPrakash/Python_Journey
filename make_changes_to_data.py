# changing data
import pandas as pd

df = pd.read_csv('pokemon_data.csv')
print(df.iloc[2])  # title of each column

# # adding a new column to sheet and also giving its value
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

print(df[['Name', 'Total']])
print('\n')

# rearranging the places of columns in data frame
cols = list(df.columns)
# print(cols)
df = df[cols[0:4] + [cols[-1]]+ cols[4:12]]
print(df.columns)  # just printing the headers
print(df)

df.to_csv('modified_pokemon_data.csv', index = False)
