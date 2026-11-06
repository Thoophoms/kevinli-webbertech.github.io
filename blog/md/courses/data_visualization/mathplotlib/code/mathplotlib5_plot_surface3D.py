import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
#fig.add_subplot(projection='3d')
ax = plt.axes(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)

plt.show()