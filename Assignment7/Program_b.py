# Gaussian Elimination

import numpy as np


def appender(matrix, y):  # Defining functions for appending, pivoting, elimination and back substtution
    matrix = np.hstack((matrix, y))  # Appends y values to matrix
    return matrix


def pivoter(matrix, i, mat_len):
    for j in range(mat_len - i):
        if abs(matrix[j + i, i]) == max(abs(matrix[i:, i])):  # Finding row containing the largest element
            matrix[[i, j + i]] = matrix[[j + i, i]]  # Pivoting
    return matrix


def eliminator(matrix, i, mat_len):
    for j in range(mat_len - i - 1):
        matrix[i + j + 1] = matrix[i + j + 1] - (matrix[i] * matrix[i + j + 1, i]) / matrix[i, i]  # Elimination
    return matrix


def back_sub(matrix, mat_len, solutions):  # Back substitution
    for i in range(mat_len):
        sum = 0
        for j in range(i):
            sum += (matrix[mat_len - i - 1, mat_len - j - 1]) * solutions[mat_len - j - 1]
        solutions[mat_len - i - 1] = (matrix[mat_len - i - 1, -1] - sum) / matrix[mat_len - i - 1, mat_len - i - 1]

    return solutions


def gauss_elm(matrix, y): # Combining all functions
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
        print(f"X{i + 1} = {round(solutions[i], 10)}")


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
