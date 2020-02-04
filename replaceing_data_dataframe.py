import pandas as pd
# import re
data = pd.DataFrame({'Employee_id': [111, 222, 333, 444], 'Employee_name': ['Rajat_mega', 'Prateema_mega', 'Malvika', 'Yash_mega'], 'salary': [29000, 32000, 34000, 27000], 'year_of_expr': [2, 4, 5, 6]})

print(data)
print('\n')

# change a particualr value for all the data frame with one go

new = data.loc[data['Employee_name'].str.contains('mega')]
print(new)
print('\n')
# remove all the _mega from Employee_name
print(data['Employee_name'].str.replace('_mega', ''))
