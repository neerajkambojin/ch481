import numpy as np

matrix = np.array([[2, 7, 9, 5],
                   [6, 8, 5, 7],
                   [7, 12, 14.0, 7],
                   [6,7,21,17]])
y = np.array([[24],
              [22],
              [33],
              [57]])

mat_len = len(matrix)

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

matrix = appender(matrix, y)
i = 0
while i < mat_len:
    matrix = pivoter(matrix, i, mat_len)
    matrix = eliminator(matrix, i, mat_len)
    i += 1

print(matrix)
