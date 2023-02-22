# Create a NumPy array.
# Access and modify elements in the array

import numpy as np
# numpy is a python library and is called as np in the program for convenience

# 2D array with shape (3, 4)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# accessing an element in the array
print(arr[1, 2])

# modify an element in the array
arr[1, 2] = 20
print(arr)

