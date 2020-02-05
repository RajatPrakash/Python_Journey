import matplotlib.pyplot as plt
import numpy as np
import random

x = np.random.randint(100)
y = np.random.randint(100)

size = plt.figure(figsize=(4, 4))
plt.scatter(x, y)
plt.show()