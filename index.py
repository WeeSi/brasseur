import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 2000)
y1 = (240 - 2.5 * x) / 7.5
y2 = (5 - 0.125 * x) / 0.125
y3 = (595 - 17.5 * x) / 10

plt.plot(x, y1, label=r'$2.5 x_{1} + 7.5 x_{2}\leq 240$')
plt.plot(x, y2, label=r'$0.125x_{1} + 0.125 x_{2}\leq 5$')
plt.plot(x, y3, label=r'$17.5x_{1} + 10 x_{2}\leq 595$')

plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')

plt.xlim(0,100)
plt.ylim(0,100)

plt.fill_between(x, 0, np.min([y1, y2, y3], axis=0), color='red', alpha=0.5, hatch='//',
                 interpolate=True, label='$intersection$')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
plt.show()