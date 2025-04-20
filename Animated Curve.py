import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Setup figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(1, 20)
ax.set_ylim(0, 400)
ax.set_xlabel('Input Size (n)')
ax.set_ylabel('Time Complexity')
ax.set_title('Big-O Complexity Classes (Animation)')

# Generate x-axis values
n = np.linspace(1, 20, 100)

# Big-O functions
O1 = np.ones_like(n)               # O(1)
O_log_n = np.log2(n)               # O(log n)
O_n = n                            # O(n)
O_n_log_n = n * np.log2(n)         # O(n log n)
O_n2 = n ** 2                      # O(n²)
O_nk = n ** 3                      # O(n^k), k=3

# Initialize empty lines
lines = {}
classes = ['O(1)', 'O(log n)', 'O(n)', 'O(n log n)', 'O(n²)', 'O(n^k)']
colors = ['green', 'blue', 'orange', 'red', 'purple', 'black']

for cls, color in zip(classes, colors):
    lines[cls], = ax.plot([], [], label=cls, lw=2, color=color)

ax.legend()

# Animation update function
def update(frame):
    current_n = n[:frame]
    lines['O(1)'].set_data(current_n, O1[:frame])
    lines['O(log n)'].set_data(current_n, O_log_n[:frame])
    lines['O(n)'].set_data(current_n, O_n[:frame])
    lines['O(n log n)'].set_data(current_n, O_n_log_n[:frame])
    lines['O(n²)'].set_data(current_n, O_n2[:frame])
    lines['O(n^k)'].set_data(current_n, O_nk[:frame])
    return lines.values()

# Create animation
ani = FuncAnimation(fig, update, frames=len(n), interval=100, blit=True)
plt.show()