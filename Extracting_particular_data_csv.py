# Extracting first name and last name from csv file and store it in a new list

import csv

new_list = []
with open('sample_file.csv') as file:
    data = csv.reader(file,delimiter=',')
    records = list(data)


for i in records[1:4]:
    new_list.append.(i[0]+' '+i[1])  #adding first name and last name  from csv file

print(new_list)
