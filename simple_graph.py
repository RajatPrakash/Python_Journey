import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = [1,2,3]
y = [2,4,6]
plt.plot(x,y)
# playing with font of title
plt.title('First graph', fontdict={'fontname':'Comic Sans MS', 'fontsize':20})
plt.xlabel('X Axis')
plt.ylabel('y Axis')
plt.show()