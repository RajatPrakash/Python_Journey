# query for numpy

"""1 1 1 1 1
   1 0 0 0 1
   1 0 9 0 1
   1 0 0 0 1
   1 1 1 1 1 create this array using numpy   
   """

import numpy as np

final_array  = np.ones((5,5))
# or final_array  = np.ones(shape = (5,5))
print(final_array)

inner_array = np.zeros((3,3))
print(inner_array)

inner_array[1][1] = 9
print('\n')
print(inner_array)
print('\n')
print('\n')
final_array[1:4,1:4] = inner_array
print('Final Result')
print(final_array)