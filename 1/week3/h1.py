import numpy as np
import math
from scipy import optimize
import matplotlib.pylab as plt

def f(x):
    return math.sin(x/5.0) * math.exp(x/10.0) + 5*math.exp(-x/2.0)

z = optimize.minimize(f, [30], method='BFGS')

ran = np.arange(0., 30., 0.1)

plt.plot(ran, [f(i) for i in ran])
plt.show()
