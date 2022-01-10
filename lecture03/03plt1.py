import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = x**2 + 2*x + 1

plt.plot(x, y, color="blue", linewidth=2, linestyle="dotted")
plt.show()
