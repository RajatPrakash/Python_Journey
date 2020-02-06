import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# showing the value of line inside the plot
x = np.arange(1,10,2)
y = np.sin(x)
plt.plot(x,y,label = 'Y = sin(x)')
plt.legend()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
