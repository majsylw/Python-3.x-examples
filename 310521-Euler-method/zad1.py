import numpy as np
import matplotlib.pyplot as plt
#from __future__ import division

# Funkcja analityczna
N = lambda t: N0 * np.exp(-k * t)

# dN/dt
def dx_dt(x):
    return - k * x

k = 1
h = 0.001

t = np.arange(0, 10, h)

for N0 in [10, 100, 1000, 10000]:
    y = np.zeros(len(t))
    y[0] = N0
    plt.figure()
    for i in range(1, len(t)):
        # Metoda Eulera
        y[i] = y[i-1] + dx_dt(y[i-1]) * h
    plt.plot(t, abs(y-N(t)),'k--', markersize=1)
    plt.plot(t, abs(y-N(t))/N(t),'b--', markersize=1)
    max_error = abs(y-N(t)).max()
    print("Różnica między dokładnym rozwiązaniem i przybliżeniem Eulera z krokiem h={0:.5}:".format(h))
    print("{0:.15}".format(max_error))
    plt.show()
