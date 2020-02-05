import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,20, 0.5)

plt.subplot(1, 3, 1)
plt.plot(x, 'r--')

plt.subplot(1, 3, 2)
plt.plot(x**2, 'g--')

plt.subplot(1, 3, 3)
plt.plot(x**3, 'y--')

plt.show()