import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(4, 4, sharex=True, sharey=False)

# Add grid lines

for a in ax.flat:
    a.grid(True, color='lightgray', linestyle='--', linewidth=0.5)

plt.show()

"""
for axi in ax.flat:
    axi.xaxis.set_major_locator(plt.MaxNLocator(3))
    axi.yaxis.set_major_locator(plt.MaxNLocator(3))
"""
