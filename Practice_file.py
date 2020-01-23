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

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = [i * 10 for i in my_list]
print(new_list)

# using list comprehension square only even elements

even_list = [i ** 2 for i in my_list if i % 2 == 0]
print(even_list)
print('\n')
# using list comprehension convert c into f (temperatures)
# formula == 9/5 * C + 32
Temp_c = [25, 30, 40, 50]
Temp_F = [(9 / 5 * i + 32) for i in Temp_c]
print('Temp Converter')
print(Temp_F)

# using list comprehension extract only number from a string

my_string = 'Hi! my name is Rajat Prakash , I am 23 year old and I will become CEO of GOOGLE'
output = [i for i in my_string if i.isdigit()]
print(output)
print('\n')
print('-----------------2020-01-23-----------------')


# create a function multiply it by 10

def mul(value):
    value = value * 10
    print(value)


mul(10)


# setting a default value to a function

def age(value=23):
    print('my age is {}'.format(value))


age() # not giving and parameter while calling the function

# lambda challenge
# create a lambda function with two parameters and multiply them

result = lambda x, y: x*y
print(result(3, 6))
