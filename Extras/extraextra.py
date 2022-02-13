import numpy as np
matrix = np.array([[0, 2, 0, 1, 0],
                   [2, 2, 3, 2, -2],
                   [4, -3, 0, 1, -7],
                   [6, 1, -6, -5, 6]], float)

for i in range(3):
    where = np.where(abs(matrix[i:, i]) == max(abs(matrix[i:, i])))
    where = where[0][0] + i
    matrix[[i, where]] = matrix[[where, i]]
    print(matrix)
    for j in range(i + 1, 3):
        matrix[j] = (matrix[j] * matrix[i][i]) / (matrix[j][i])
        if matrix[j][i] - matrix[i][i] == 0:
            matrix[j] = matrix[j] - matrix[i]
        else:
            matrix[j] = matrix[j] - matrix[i]
        print(matrix)
    if j == 1:
        break
