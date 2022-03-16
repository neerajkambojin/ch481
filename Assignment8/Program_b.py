# M = P.L.U
import numpy as np


def pivote_pi(matrix, i, mat_len):
    global pi
    pi = np.identity(mat_len)
    for j in range(mat_len - i):
        if abs(matrix[j + i, i]) == max(abs(matrix[i:, i])):  # Finding row containing the largest element
            matrix[[i, j + i]] = matrix[[j + i, i]]  # Pivoting
            pi[[i, j + i]] = pi[[j + i, i]]
    return matrix, pi


def eliminate_li(matrix, i, mat_len):
    global li
    li = np.identity(mat_len)
    for j in range(mat_len - i - 1):
        fact = (matrix[i + j + 1, i]) / matrix[i, i]
        matrix[i + j + 1] -= (matrix[i] * fact)  # Elimination
        li[i + j + 1, i] = fact
    return matrix, li


def lu_decompose(matrix):
    mat_len = len(matrix)
    ptot = np.identity(mat_len)
    ltot = np.identity(mat_len)
    for i in range(mat_len):
        pivote_pi(matrix, i, mat_len)
        ptot = np.matmul(ptot, pi)
        eliminate_li(matrix, i, mat_len)
        ltot = np.matmul(pi, np.matmul(ltot, np.matmul(pi, li)))
    print("P: ")
    print(ptot)
    print("L: ")
    print(ltot)
    print("U: ")
    print(matrix)
    print("Original Matrix (P.L.U): ")
    print(np.matmul(ptot, np.matmul(ltot, matrix)))


try:
    mat_len = int(input("Number of unknowns (Hit enter to take provided matrix): "))
    matrix = np.empty((mat_len, mat_len))
    y = np.empty((mat_len, 1))
    for i in range(mat_len):
        for j in range(mat_len):
            matrix[i, j] = float(input(f"A{i + 1}{j + 1}: "))
except ValueError:
    matrix = np.array([[3, -2, 1],
                       [-4, -1, 4],
                       [1, -1, 3.0]])

lu_decompose(matrix)
