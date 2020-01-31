# for slicing and indexing
import numpy as np

multi_dimensional_array = np.random.randint(10, size=(2, 3))
print(multi_dimensional_array)
print('\n')

# element at index 0
print('Element at index 0 is ')
print(multi_dimensional_array[0][0])
print('\n')

# element at index 2 row 3 column
print("Element at 2 row and 3 column is ")
print(multi_dimensional_array[1][2])
print('\n')


# slicing getting only a part of the code
print(multi_dimensional_array[:, 1:])