# linera algebra with matrices
# condition (n?,k),(k,m?)->(n?,m?)
import numpy as np

first = np.array([1,2]) # size - 1,2 i:e n=1 and k =2
second = np.array([[5,6,7],[2,3,5]]) # size - 2,3 i:e k=2 and m =3

print(first)
print(second)
print('\n')
result = np.matmul(first,second)  # size - 1,3  i:e n = 1 and m =3
print(result)
