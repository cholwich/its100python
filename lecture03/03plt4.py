import numpy as np
import matplotlib.pyplot as plt
import math as m

x = np.arange(-m.pi*2, m.pi*2, 0.1)
y1 = np.cos(x)
y2 = np.sin(x)

plt.plot(x, y1, color="blue", linewidth=2, linestyle="dashed")
plt.plot(x, y2, color="orange", linewidth=2)
plt.xlim(-20, 20)
plt.show()
