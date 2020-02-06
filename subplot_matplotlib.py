import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# creating multiple graph into a single plot

x = np.arange(1,100, 5)
# y = x
plt.subplot(1, 3, 1)
plt.plot(x, np.sin(x), 'g--')

plt.subplot(1, 3, 2)
plt.plot(x, np.cos(x), 'r--')

plt.subplot(1, 3, 3)
plt.plot(x, np.tan(x), 'y--')


plt.show()
