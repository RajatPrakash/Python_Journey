import pandas as pd

# data = pd.DataFrame({'Employee_id': [111, 222, 333, 444], 'Employee_name': ['Rajat', 'Prateema', 'Malvika', 'Yash'], 'salary': [29000, 32000, 34000, 27000], 'year_of_expr': [2, 4, 5, 6]})

data = pd.DataFrame({'Student_name':['akash', 'mansi', 'roshan', 'chandu'], 'age': [15, 17, 19, 14]
, 'subject': ['maths', 'english', 'physics', 'computer science']})

print(data)
print('\n')

# applying only the single condition on data
print('Filter student details of maths subject only')
print(data.loc[data['subject'] == 'maths'])
print('\n')

# applying multiple condition on data
print('Filter student details of maths and physics subject only')
print(data.loc[(data['subject'] == 'maths') & (data['subject'] == 'physics')])  # no data exists

new_data = data.loc[(data['subject'] == 'maths') | (data['subject'] == 'physics')]
print(new_data)


# reset index -- after filter and saving data gets stored in old indexing format
new_data = new_data.reset_index()
print(new_data)
# In normal python we use AND OR NOT but in pandas we use the actual symbols &, |, !