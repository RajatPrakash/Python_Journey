# changing data
import pandas as pd

df = pd.read_csv('pokemon_data.csv')
print(df.iloc[2])  # title of each column

# # adding a new column to sheet and also giving its value
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

print(df[['Name', 'Total']])
