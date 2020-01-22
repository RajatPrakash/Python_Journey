# print every fruits except orange
my_list = ['apple', 'mango', 'blueberry', 'Kiwi', 'orange']

# One Way
for i in my_list[0:4]:
    print(i)

    # this will provide desire result but this
    # is not the optimal solution since we know the list so we can put limit
print('\n')
# second way more suitable
for i in my_list:
    if i == 'orange':
        continue
    print(i)
    # orange can be placed anywhere and code it completely ignore it

# using list comprehension multiply each element by 10

my_list = [1, 2, 3, 4, 5]

new_list = [i * 10 for i in my_list]
print(new_list)
