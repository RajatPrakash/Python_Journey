# using built in methods in arrays

import numpy as np

# Create a random array of  numbers
my_array = np.random.rand(10) #length of array
print(my_array)

# create a random array of integer numbers
my_int_arrray = np.random.randint(1,100,10)  #(range,count)
print(my_int_arrray)

# multidimensinal array of random number
multi_random = np.random.rand(10,10)
print(multi_random)

# arrange array in sequence 

arrange_array = np.arange(10,50)
print(arrange_array)


# arrange sequence of array with a step of 4
arrange_step_array = np.arange(1,100,10)
print(arrange_step_array)

# create a arrray with all 1's at diagonal
arr = np.eye(5)
print(arr)


# create a array with all element zero and one
zero = np.zeros(shape=(5,5))
one = np.ones(shape = (5,5))

print(zero)
print(one)