# scatter plot chart

import numpy as np
import matplotlib.pyplot as plt

# sample data
x = np.random.rand(50)
y = np.random.rand(50)

# scatter plot
plt.scatter(x, y)

# labels and title
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot")

# display chart
plt.show()
