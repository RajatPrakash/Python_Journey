# mathematics with array in numpy

import numpy as np
print('Orignal Array')
my_array = np.array([1,2,3,4,5,6])
print(my_array)
print('\n')

# addition
my_array = my_array+2
print('After Addition array')
print(my_array)
print('\n')

# substraction
my_array = my_array-10
print('After Substraction Array')
print(my_array)
print('\n')

# multiplication
my_array = my_array *-15
print('After multipication Array')
print(my_array)
print('\n')

# division
my_array = my_array / 10
print('After Division Array')
print(my_array)
print('\n')

# modulus
my_array = my_array % 4
print('After Modulus Array')
print(my_array)
print('\n')

# power of a array
my_array = my_array **2
print('After power of 2 Array')
print(my_array)
print('\n')

# addition of two array
first = np.array([1,2,3,4,5])
second = np.array([9,8,7,6,5])
print('addition of two array')
print('first array:',first)
print('second array:',second)
print('adition of above two array',first+second)
print('\n')