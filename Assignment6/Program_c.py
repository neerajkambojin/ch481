import numpy
import numpy as np
matrix = np.array([[0, 2, 0, 1, 0],
                   [2, 2, 3, 2, -2],
                   [4, -3, 0, 1, -7],
                   [6, 1, -6, -5, 6]], float)

for i in range(3):
        where = np.where(abs(matrix[:, i]) == max(abs(matrix[:, i])))
        matrix[[i, where[0][0]]] = matrix[[where[0][0], i]]
        matrix[i] = matrix[i] / matrix[i][i]
        matrix[i+1] = matrix[i+1] - matrix[i+1][i]*matrix[i]
        # print(matrix)
        print(matrix)

# print(np.where(matrix[:,0] == 6)[0][0])
# print(matrix)
# matrix[[0,3]] = matrix[[3,0]]
# print(matrix)
# print(np.fabs(-4))