import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# showing the value of line inside the plot
x = np.arange(1,100,10)
y = np.sin(x)
plt.plot(x, y, label='Y = sin(x)', linewidth=1.5, marker='*', markersize=5)
plt.legend()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
