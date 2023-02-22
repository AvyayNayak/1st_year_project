# Create a 2-dimensional array and check the shape of the array
# Access elements from the 2D array using index positions

import numpy as np

# 2D array with 3 rows and 4 columns
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# shape of the array
print("Array shape:", arr.shape)

# Access element at row index 1, column index 2
print("Element at row 1, column 2:", arr[1, 2])
