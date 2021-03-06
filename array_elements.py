# accessing array elements rows/columns
import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [9, 8, 7, 6, 5, 4, 3]])
print(a.shape)  # array shape
print(a)
print('\n')

# specific array element [r,c]
# item 6
print(a[0][5])

# item 8
print(a[1][1])  # or
print(a[1][-6])

# get a specific row/specific column
print(a[1])
print(a[0])
print(a[0, :])
print(a[:, 1])  # prints second column
print('\n')

# get only the even numbers from first row [start_index:end_index:step]
print('even numbers from first row')
print(a[0, 1:8:2])

# change certain value of array
a[1, 2] = 90
print('new array is ',a)