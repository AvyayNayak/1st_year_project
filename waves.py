import matplotlib.pyplot as plt
import numpy as np

# create x values
x = np.linspace(0, 10, 100)

# create y values for two lines
y1 = np.sin(x)
y2 = np.cos(x)

# plot both lines on the same plot
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')

# set plot title and axis labels
plt.title('Sin and Cos Functions')
plt.xlabel('x')
plt.ylabel('y')

# add legend
plt.legend()

# display plot
plt.show()
