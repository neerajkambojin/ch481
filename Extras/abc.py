import numpy as np

arr = np.empty((5,5))
for i in range(1,6):
    for j in range(1,6):
        arr[i-1][j-1] = i**2 + j + 1
