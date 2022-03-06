import numpy as np

def appender(matrix, y):
    matrix = np.hstack((matrix, y))
    return matrix

def pivoter(matrix, i, mat_len):
    for j in range(mat_len - i):
        if abs(matrix[j + i, i]) == max(abs(matrix[i:, i])):
            matrix[[i, j + i]] = matrix[[j + i, i]]
    return matrix

def eliminator(matrix, i, mat_len):
    for j in range(mat_len - i - 1):
        matrix[i + j + 1] = matrix[i + j + 1] - (matrix[i] * matrix[i + j + 1, i]) / matrix[i, i]
    return matrix

matrix = np.array([[3, -2, 1],
                   [-4, -1, 4],
                   [1, -1, 3.0]])
y = np.array([[15],
              [8],
              [13]])

mat_len = len(matrix)

matrix = appender(matrix, y)

i = 0
while i < mat_len:
    matrix = pivoter(matrix, i, mat_len)
    matrix = eliminator(matrix, i, mat_len)
    i += 1

print(matrix)


