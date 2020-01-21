# QUESTION:Write a code to select DICTIONARY elements that are greater then or equal to 30 and place the values in a
# LIST
my_dict = {'key1': 21, 'key2': 45, 'key3': 55, 'key4': 14, 'key5': 26}
value = 30
list_value =[]

for i,j in my_dict.items():
    if j >= value:
        print(f'Key: ', i, 'Value :', j)
        list_value.append(j)

print(list_value)