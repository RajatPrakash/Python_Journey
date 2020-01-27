# remove all the spaces and special character froma a file
import re
with open('fruits_input.txt','r') as file:
    each_line = file.readlines()

with open('new_file2.txt', 'w') as new_file:
    new = [item.strip(' ') and item.strip('\n') and item.strip('!') and item.strip('@') and item.strip('$') and item.strip('%') and item.strip('^') and item.strip('&') and item.strip('*') for item in each_line]
    new_file.writelines(new)

file.close()
new_file.close()