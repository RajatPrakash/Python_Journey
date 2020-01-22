# generate a new list with the square of each element

my_list = [1, 2, 3, 4, 5, 6]

new_list = []

for i in my_list:
    element = i**2
    new_list.append(element)

print(new_list)

# another more elegant way is LIST COMPREHENSIO

new_list_2 = [element**2 for element in my_list]
print(new_list_2)