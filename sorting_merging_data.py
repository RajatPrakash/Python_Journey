import pandas as pd

data = pd.DataFrame({'Employee_id': [111, 222, 333, 444], 'Employee_name': ['Rajat', 'Prateema', 'Malvika', 'Yash'], 'salary': [29000, 32000, 34000, 27000], 'year_of_expr': [55, 46, 21, 6]})
print(data)

# sorting

print(data.sort_values(by='year_of_expr'))
print(data)
print('\n')

# sorting and merging data

data.sort_values(by='year_of_expr', inplace=True)
print(data)