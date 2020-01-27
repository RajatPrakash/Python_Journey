# remove all the spaces and special character froma a file
import re

with open('fruits_input.txt', 'r') as file:
    each_line = file.readlines()

with open('new_file2.txt', 'w') as new_file:
    new = [item.replace(' ', '') and item.replace('\n', '') and item.replace('!', '') and item.replace('%', '') for item in each_line]
    new_file.writelines(new)
    print(new)

file.close()
new_file.close()
