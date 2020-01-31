# for slicing and indexing
import numpy as np

multi_dimensional_array = np.random.randint(10, size=(5, 5))
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


# slicing getting only a part of the  code (bottom half of code)
print(multi_dimensional_array[2:])
print('\n')

# slicing to get top 2 rows and only some columns
print(multi_dimensional_array[:2, 1:3])
print('\n')

# challenge: extract the middle value from the 5x5 matrix
print('Center value of matrix is:')
print(multi_dimensional_array[2:3, 2:3])
print('\n')


# get the center column from 5X5 matrix

print('center column from  matrix is ')
print(multi_dimensional_array[:, 2:3])
