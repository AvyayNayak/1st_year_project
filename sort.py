# sorting an array
import numpy as np

# 2D numpy array
arr = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])

# sorting array along the row
arr.sort(axis=1)
# If the axis parameter is changed to 0, the np.sort function will sort the columns of the 2D array in ascending order

# print the sorted array
print(f'the sorted array is \n{arr}')
