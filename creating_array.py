import numpy as np

my_list = list(range(0,10))
print(my_list*2)

my_array = np.array(my_list)
print(my_array)

print(type(my_array*2))