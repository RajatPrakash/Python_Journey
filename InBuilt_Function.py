# lambda function
import random
from functools import reduce
test = (lambda x: x ** 2)  # square of a number

# user_input = int(input('Enter any Number:'))
# print(test(user_input))


# Map function will do the same thing on every element of the list
new = list(range(0, 100))  # Random list
print(list(map(test, random.sample(new, 8))))


# filter will perform the same function on each item of list generate the new list accordingly

print(list(filter(lambda x: x % 2 == 0, random.sample(new, 10))))

# converting Celsius into fahrenheit

celsius = [23, 57, 42, 104, 18]

fahrenheit = list(map(lambda x: (float(9/5)) * x + 32, celsius))
print(fahrenheit)

# Reduce function

my_list = list(range(10))

print(reduce(lambda x, y: (x**2) + y, my_list))