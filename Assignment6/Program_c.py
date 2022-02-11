import numpy as np
matrix = np.array([[0, 2, 0, 1, 0],
                   [2, 2, 3, 2, -2],
                   [4, -3, 0, 1, -7],
                   [6, 1, -6, -5, 6]])

if matrix[0][0] == 0:
    for j in matrix:
        if j[0] == max(matrix[:, 0]):
            matrix[0] = j

print(matrix)
