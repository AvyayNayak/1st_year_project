# bar graph

import numpy as np
import matplotlib.pyplot as plt

# sample data
x = np.array(["A", "B", "C", "D"])
y = np.array([20, 55, 44, 66])

# bar chart
plt.bar(x, y)

# labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Graph")

# display chart
plt.show()
