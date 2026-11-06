import matplotlib.pyplot as plt
import numpy as np

# Create a 2x2 grid of subplots
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x**2
y4 = np.sqrt(x)

# Plot data on each subplot
ax[0, 0].plot(x, y1, color='red')
ax[0, 0].set_title('Subplot 1')
ax[0, 0].grid(True, color='lightgray', linestyle='--', linewidth=0.5)
ax[0, 1].plot(x, y2, color='blue')
ax[0, 1].set_title('Subplot 2')
ax[0, 1].grid(True, color='lightgray', linestyle='--', linewidth=0.5)
ax[1, 0].plot(x, y3, color='green')
ax[1, 0].set_title('Subplot 3')
ax[1, 0].grid(True, color='lightgray', linestyle='--', linewidth=0.5)
ax[1, 1].plot(x, y4, color='purple')
ax[1, 1].set_title('Subplot 4')
ax[1, 1].grid(True, color='lightgray', linestyle='--', linewidth=0.5)

# Adjust layout and display the plot

plt.tight_layout()
plt.show()