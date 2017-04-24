#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

delta = 0.025
x1 = np.arange(-2.0, 8.0, delta)
x2 = np.arange(-3.0, 7.0, delta)
X1, X2 = np.meshgrid(x1, x2)
# Objective Function
Z = (X1 - 3)**2 + (X2 - 2)**2
c1_x2 = x1**2 - 3
c2_x2 = 1.0


plt.figure()
plt.title('Minimization problem w. constrains')
CS = plt.contour(X1, X2, Z, [0.5] + list(np.arange(2, 45, 5.0)))
plt.clabel(CS, inline=1, fontsize=10)

plt.plot(x1, c1_x2, label='constrain 1', color='red')
#  plt.fill_between(x1, c1_x2, 7.0, where=(c1_x2 <= 7.0),
#                   interpolate=True, facecolor='red', alpha=0.3)
plt.plot(x1, c2_x2 * np.ones(x1.shape), label='constrain 2', color='cyan')
#  plt.fill_between(x1, -3.0, c2_x2,
#                   interpolate=True, facecolor='cyan', alpha=0.3)
plt.plot(np.zeros(x2.shape), x2, label='constrain 3', color='yellow')
#  plt.fill_between(x1, -3.0, 7.0, where=(x1 >= 0),
#                   interpolate=True, facecolor='yellow', alpha=0.3)
plt.fill_between(x1, c1_x2, c2_x2, where=(c1_x2 <= c2_x2) * (x1 >= 0),
                 interpolate=True, facecolor='orange', alpha=0.3)

# Plot unconstrained global minimum
plt.plot(3.0, 2.0, marker='o', label='min w/o constrains')
# Plot constrained minimum
plt.plot(2.0, 1.0, marker='*', color='black', label='min w. constrains')

plt.tick_params(axis='both', direction='out')
plt.xticks(np.arange(-2.0, 8.0 + 1, 1.0))
plt.yticks(np.arange(-3.0, 7.0 + 1, 1.0))
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-2.0, 8.0)
plt.ylim(-3.0, 7.0)

plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()

#  plt.show()
plt.savefig("02-minimize-1.png", bbox_inches='tight', dpi=150)
