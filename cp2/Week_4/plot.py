import matplotlib.pyplot as plt
import numpy as np

# Create grid lines from 0 to 7
x = np.arange(0, 8, 1)
y = np.arange(0, 8, 1)

# Draw grid
for i in x:
    plt.plot([i, i], [0, 7], color="black")  # vertical lines
for j in y:
    plt.plot([0, 7], [j, j], color="black")  # horizontal lines

plt.xticks(range(8))
plt.yticks(range(8))
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

