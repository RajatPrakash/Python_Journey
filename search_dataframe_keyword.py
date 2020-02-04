# search data frame using a particular keyword
import pandas as pd

data = pd.DataFrame({'Employee_id': [111, 222, 333, 444], 'Employee_name': ['Rajat_mega', 'Prateema_mega', 'Malvika', 'Yash_mega'], 'salary': [29000, 32000, 34000, 27000], 'year_of_expr': [2, 4, 5, 6]})

print(data)
print('\n')

# print data by searching only the particular keyword in data frame

search = data.loc[data['Employee_name'].str.contains('mega')]
print(search)
print('\n')

search1 = data.loc[~data['Employee_name'].str.contains('mega')]
print(search1)