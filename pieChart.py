# pie  chart

import numpy as np
import matplotlib.pyplot as plt

# sample data
labels = np.array(["A", "B", "C", "D"])
sizes = np.array([28, 82, 124,45])

# creating pie chart
plt.pie(sizes, labels=labels)

# adding title
plt.title("Pie Chart")

# displaying chart
plt.show()
