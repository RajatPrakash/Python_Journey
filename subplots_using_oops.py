import matplotlib.pylab as plt
import numpy as np

fig, axes = plt.subplots(nrows=3, ncols=1)

axes
x = [1, 2, 3, 4, 5, 6, 7]
y = np.sin(x)

axes[0].plot(x, y, 'r')
axes[0].set_xlabel('value of x')
axes[0].set_ylabel('sin of x')
axes[0].set_title('First Graph')

axes[1].plot(x, y**2, 'r')
axes[1].set_xlabel('value of x')
axes[1].set_ylabel('square of x')
axes[1].set_title('second Graph')

axes[2].plot(x, y**3, 'r')
axes[2].set_xlabel('value of x')
axes[2].set_ylabel('cube of x')
axes[2].set_title('Third Graph')

plt.show()