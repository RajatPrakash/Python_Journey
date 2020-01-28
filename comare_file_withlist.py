# READ THE FILE 'FRUITS_INPUT.TXT'
# AND COMPARE IT TO THE LIST OF FRUITS IN MY_FRUITS,
# RETURN ONLY MATCHING ELEMENTS

my_list =['Apricot', 'Avocado', 'Banana', 'Bilberry', 'Blackberry', 'Cherry', 'Feijoa']
output = []

with open('fruits_input.txt', 'r') as file:
    data = file.readlines()

for i in data:
    if i in my_list:
        output.append(i)

print(output)