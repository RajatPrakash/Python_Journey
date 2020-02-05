import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.5) # evenly sampled time at 0.5 sec
y = np.sin(x)

# print(x)
# print('\n')
# print(y)
plt.xlabel('Time')
plt.ylabel('Sin Wave')
plt.title('Plotting exercise')
plt.plot(x, y)
plt.show()