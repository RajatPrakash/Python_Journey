# apply function on data using pandas

import pandas as pd

data = pd.DataFrame({'Employee_id': [111, 222, 333, 444], 'Employee_name': ['Rajat', 'Prateema', 'Malvika', 'Yash'], 'salary': [29000, 32000, 34000, 27000], 'year_of_expr': [2, 4, 5, 6]})
print(data)
print('\n')

# column names:   Employee_id Employee_name  salary  year_of_expr


def salary(number):
    return number + 1000


def name_len(name):
    length = len(name)
    return length


# applying function on salary column
print(data['salary'].apply(salary))
print('\n')

# apply function on name column
print(data['Employee_name'].apply(name_len))
