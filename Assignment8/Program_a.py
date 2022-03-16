# M = P.L.U


def pivoter(matrix, i, mat_len):
    for j in range(mat_len - i):
        if abs(matrix[j + i, i]) == max(abs(matrix[i:, i])):  # Finding row containing the largest element
            matrix[[i, j + i]] = matrix[[j + i, i]]  # Pivoting
    return matrix


def eliminator(matrix, i, mat_len):
    for j in range(mat_len - i - 1):
        matrix[i + j + 1] = matrix[i + j + 1] - (matrix[i] * matrix[i + j + 1, i]) / matrix[i, i]  # Elimination
    return matrix


import numpy as np

matrix = np.array([[3, -2, 1],
                   [-4, -1, 4],
                   [1, -1, 3.0]])

mat_len = int(input("Number of unknowns: "))

ptot = np.identity(mat_len)
ltot = np.identity(mat_len)

for i in range(mat_len):
    tmp = matrix.copy()
    pivoter(matrix, i, mat_len)
    pi = np.matmul(matrix, np.linalg.inv(tmp))
    print(pi)
    break