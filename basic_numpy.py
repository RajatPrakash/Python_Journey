import numpy as np

# 1d array:
a = np.array([1, 2, 3, 4])
print('1-d array ')
print(a)
print(' \n')

# 2d array:
print('2-d array ')
b = np.array([[1.2, 3.2, 1.4], [1.1, 2.2, 3.3]])
print(b)
print(' \n')


# get the dimension of the array
print(f'a is {a.ndim}d array')
print(f'b is {b.ndim}d array')

# get shape of the array, shape is vector
print(f'a is {a.shape}')
print(f'b is {b.shape}')