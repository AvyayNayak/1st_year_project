# appending elements into an array

import numpy as np

# 1D numpy array
arr = np.array([1, 2, 3])

# appending an element to the array
arr = np.append(arr, 4)

print(arr)

# appending multiple elements to the array
arr = np.append(arr, [5, 6, 7])

# printing the modified array
print(arr)