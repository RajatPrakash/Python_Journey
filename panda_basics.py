import pandas as pd

my_list = ['watermelon','orange','apple']
label = ['fruit#1', 'fruit#2', 'fruit#3']

x = pd.Series(data=my_list, index=label)
print(x)