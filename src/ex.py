import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


x = np.arange(0.0, 50.0, 2.0)
y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
sizes = np.random.rand(*x.shape) * 800 + 500

print(f"x type {type(x)}: {x}")
print(f"y type {type(y)}: {y}")


fig, ax = plt.subplots()
ax.scatter(x, y, sizes, c="green", alpha=0.5, marker=r'$\clubsuit$',
           label="Luck")
ax.set_xlabel("Leprechauns")
ax.set_ylabel("Gold")
ax.legend()
plt.show()