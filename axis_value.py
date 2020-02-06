import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# removing decimcal from x-axis and y - axis values
x = [10,20,30,40,50]
y = [20,40,60,80,100]
plt.plot(x,y)
# playing with font of title
plt.title('Removing Decimal from Axis', fontdict={'fontname':'Comic Sans MS', 'fontsize':10})
plt.xlabel('X Axis')
plt.ylabel('y Axis')
plt.xticks([10, 20, 30, 40, 50])  # this is will be the exact values shows on axis
plt.yticks([20,40,60,80,100]) # same (removed all the deafult values)
plt.show()