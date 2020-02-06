import matplotlib.pyplot as plt
import random as r

x = [1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,3,4,5,6,7]

num_bins = 5

n, bins, patches = plt.hist(x, num_bins, facecolor='red')
plt.show()