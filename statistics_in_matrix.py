# statistics in matrix

import numpy as np

arr =np.array([[1,2,3,4],[5,-3,7,8]])
print('original array')
print(arr)
print('\n')

# Min element in array
print('Min element in array')
print(np.min(arr))
print('Min element of axis 0',np.min(arr,axis=0)) # axis=0 means min element among each column
print('\n')
print('Min element of axis 1',np.min(arr,axis=1)) # axis=1 means min element among each row


# similarly max element in array
print('\n')
print('max elemement in array')
print('max element among the whole array',np.max(arr))
print('max element among all the rows',np.max(arr,axis = 1))
print('max element among all the columns',np.max(arr,axis = 0))
print('\n')

# sum of all the elements in array
print('sum of all the element in arrray: ',np.sum(arr))