# accessing array elements rows/columns
import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [9, 8, 7, 6, 5, 4, 3]])
print(a.shape)  # array shape

# specific array element [r,c]
# item 6
print(a[0][5])

# item 8
print(a[1][1])  # or
print(a[1][-6])