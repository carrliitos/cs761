import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) with a=1, b=0
def f(x):
  return np.where(x < 0, x, x - x**2)

# Generate x values
x_values = np.linspace(-2, 2, 400)
y_values = f(x_values)

# Plot the function
plt.figure(figsize=(6, 4))
plt.plot(x_values, y_values, color='b')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.scatter(0, 0, color='red', zorder=3, label="Point of continuity")
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Graph of $f(x)$ with $a=1, b=0$")
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig("./graph.png", dpi=300)
plt.show()
