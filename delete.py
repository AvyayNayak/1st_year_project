# deleting elements in an array
import numpy as np

# 1D numpy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# deleting the elements at indexes 1, 3, and 5
indexes = [1, 3, 5]
arr = np.delete(arr, indexes)

# resulting array
print(arr)