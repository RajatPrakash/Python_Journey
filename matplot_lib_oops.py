import numpy as np
import matplotlib.pyplot as plt

figure = plt.figure(figsize=(10, 10))  # creating a simple figure
axes = figure.add_axes([0, 0, 1, 1])

x = np.linspace(0, 10, 100)
y = np.tan(x)
axes.plot(x, y, 'r--', label= 'Red Sine Wave #01')
axes.set_xlabel('Time')
axes.set_ylabel('Sine wave')
axes.set_title('My third plot')
axes.legend()
axes.set_ylim([-1, 1])        # set x and y limits
axes.set_xlim([0, 10])
axes.grid()
plt.plot(x, y)
plt.show()