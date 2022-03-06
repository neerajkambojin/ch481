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


def back_sub(matrix, mat_len, solutions):
    for i in range(mat_len):
        sum = 0
        for j in range(i):
            sum += (matrix[mat_len - i - 1, mat_len - j - 1]) * solutions[mat_len - j - 1]
        solutions[mat_len - i - 1] = (matrix[mat_len - i - 1, -1] - sum) / matrix[mat_len - i - 1, mat_len - i - 1]

    return solutions


def gauss_elm(matrix, y):
    mat_len = len(matrix)
    print("Matrix: \n", matrix)
    print("Y: \n", y)
    matrix = appender(matrix, y)

    i = 0
    while i < mat_len:
        matrix = pivoter(matrix, i, mat_len)
        matrix = eliminator(matrix, i, mat_len)
        i += 1

    solutions = np.zeros((mat_len))
    solutions = back_sub(matrix, mat_len, solutions)

    print("Solutions: ")
    for i in range(mat_len):
        print(f"X{i + 1} = {solutions[i]}")


try:
    mat_len = int(input("Number of unknowns (Hit enter to take provided matrix): "))
    matrix = np.empty((mat_len, mat_len))
    y = np.empty((mat_len, 1))
    for i in range(mat_len):
        for j in range(mat_len):
            matrix[i, j] = float(input(f"A{i + 1}{j + 1}: "))
    for i in range(mat_len):
        for j in range(1):
            y[i, j] = float(input(f"Y{i + 1}: "))
except ValueError:
    matrix = np.array([[3, -2, 1],
                       [-4, -1, 4],
                       [1, -1, 3.0]])
    y = np.array([[15],
                  [8],
                  [13]])

gauss_elm(matrix, y)
