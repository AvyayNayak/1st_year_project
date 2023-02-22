#mean , median, mode and variance

import numpy as np

# array of values
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# mean
mean = np.mean(arr)
print("Mean:", mean)

# median
median = np.median(arr)
print("Median:", median)

# standard deviation
std_dev = np.std(arr)
print("Standard Deviation:", std_dev)

# variance
variance = np.var(arr)
print("Variance:", variance)
