import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.5)  # x sample size with every 0.5 interval
size = plt.figure(figsize=(5, 5))
plt.plot(x, x, 'r--', x, x**2, 'bs', x, x**3, 'g^', linewidth=5) # red dashes, blue squares and green triangles
plt.show()