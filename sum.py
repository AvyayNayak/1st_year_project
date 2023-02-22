# summing along rows and columns

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Sum along the column
ColSum = np.sum(arr, axis=0)
print(f'sum along the column : {ColSum}')

# Sum along the row
RowSum = np.sum(arr, axis=1)
print(f'sum along the row : {RowSum}')
