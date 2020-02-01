# using pandas operation on data frame

import pandas as pd

df = pd.DataFrame({'Employee_id': [111, 222, 333, 444], 'Employee_name': ['Rajat', 'Prateema', 'Malvika', 'Yash'], 'salary': [29000, 32000, 34000, 27000], 'year_of_expr': [2, 4, 5, 6]})
print(df)
print('\n')
# accessing data based on the condidition : accessing data of employee whose exp is 2

df_new = df[(df['year_of_expr']==2)]
print('Data of employees whose year_of_expr is 2')
print(df_new)
print('\n')
# deleting a colummn from dataframe
del df['Employee_id']
print('DATA FRAME after deleting a column')
print(df)