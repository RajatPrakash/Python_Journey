# WRITE A CODE THAT TAKES A STRING AND CALCULATES THE NUMBER OF UPPER AND LOWER CASE CHARACTERS IN IT
import re
user_string = input('Enter string: ')
count_upper = 0
count_lower = 0

for i in user_string:
    if i.islower():
        count_lower += 1
    elif i.isupper():
        count_upper +=1
    else:
        continue
print('Total Number of Upper charater: {}, total number of lower  character: {}'.format(count_upper, count_lower))