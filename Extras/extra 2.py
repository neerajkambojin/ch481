import numpy as np
matrix = np.array([[0, 2, 0, 1, 0],
                   [2, 2, 3, 2, -2],
                   [4, -3, 0, 1, -7],
                   [6, 1, -6, -5, 6]], float)


print(np.where(abs(matrix[1:,1]) == max(abs(matrix[1:,1]))))
