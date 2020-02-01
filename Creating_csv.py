# creating a csv file using pandas

import pandas as pd


data = pd.DataFrame({'employee':[111, 222, 333], 'Name': ['Rajat', 'Aryan', 'Aniket'], 'age': [24, 25, 26]})

data.to_csv('sample_output', index_label=False)

# open the newly created file using pandas

file = pd.read_csv('sample_output')

print(file)