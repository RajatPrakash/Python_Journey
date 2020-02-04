# using group by function on data frame

import pandas as pd

data = pd.read_csv('modified_pokemon_data.csv')
print(data.columns)

print(data.groupby(['Type 1']).mean().sort_values(['Legendary'], ascending=False))  # sorting max legendary value on top
