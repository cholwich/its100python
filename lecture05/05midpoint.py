import matplotlib.pyplot as plt
import numpy as np

N = 10

x = np.arange(0, 2.01, 0.1)
y = x**3 + 2

x_mid = np.arange(0, 2.01, 2/N)
x_mid = (x_mid[:-1] + x_mid[1:]) / 2
y_mid = x_mid**3 + 2

plt.bar(x_mid, y_mid, width=2/N, alpha=0.2, edgecolor="blue")
plt.plot(x, y, color="blue", linewidth=2)
plt.scatter(x_mid, y_mid, color="blue")
plt.xticks(np.arange(0, 2.01, 2/N))
plt.show()
