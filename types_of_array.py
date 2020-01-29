import numpy as np

# all zeros
zero = np.zeros((2, 4))
print(zero)
print('\n')
# all ones
one = np.ones((5, 5))
print(one)
print('\n')
# any other number array
any = np.full((2, 2), 33)  # it takes two parameter shape and value
print(any)
print('\n')

# random number array
random_array = np.random.rand(2, 3)
print(random_array)