# remove all the spaces and special character froma a file
import re

with open('fruits_input.txt', 'r') as file:
    each_line = file.readlines()

with open('new_file2.txt', 'w') as new_file:
    new = [item.strip('\n') for item in each_line if '\n' in each_line]
    # new = [item.strip('!') for item in each_line if '!' in each_line]
    new_file.writelines(new)
    print(new)

file.close()
new_file.close()
