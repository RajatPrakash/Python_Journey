# opening csv file using python
import csv
with open('sample_file.csv') as csvfile:
    output = csv.reader(csvfile, delimiter=',')
    print(list(output))