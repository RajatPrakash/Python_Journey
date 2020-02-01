#creating first data frame

import pandas as pd

first_df = pd.DataFrame({'employee':[111, 222, 333], 'Name': ['Rajat', 'Aryan', 'Aniket'], 'age': [24, 25, 26]})

print(first_df)
print('\n')

# accessing the first two rows of data frame
print('First two rows')
print(first_df.head(2))
print('\n')

# accessing the last row only
print('Last one row')
print(first_df.tail(1))