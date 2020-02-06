import matplotlib.pylab as plt
import numpy as np

fig = plt.figure()
axis1 = fig.add_axes([.1, .1, .9, .9])
axis2 = fig.add_axes([0.2, 0.2, 0.3, 0.3])

x = np.linspace(0, 10, 100)
y = x*2
# axis 1 details
axis1.plot(x, y, 'r--')
axis1.set_xlabel('Value of X')
axis1.set_ylabel('X*2')
axis1.set_title('Multiple Plots')

# axis 2 details
axis2.plot(x, y**2, 'g')
axis2.set_xlabel('Value of x')
axis2.set_ylabel('Square of x')
axis2.set_title('Inner Plot')
axis1.legend()


plt.show()
