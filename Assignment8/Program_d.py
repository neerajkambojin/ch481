# M = P.L.U
import numpy as np
import random


def pivote_pi(matrix, i, mat_len):  # Function for pivoting and generating permutation matrix Pi
    global pi
    pi = np.identity(mat_len)  # Initializing Pi
    for j in range(mat_len - i):
        if abs(matrix[j + i, i]) == max(abs(matrix[i:, i])):  # Finding row containing the largest element
            matrix[[i, j + i]] = matrix[[j + i, i]]  # Pivoting
            pi[[i, j + i]] = pi[[j + i, i]]  # Generating Pi
    return matrix, pi


def eliminate_li(matrix, i, mat_len):  # For elimination and Li
    global li
    li = np.identity(mat_len)  # Initializing Li
    for j in range(mat_len - i - 1):
        fact = (matrix[i + j + 1, i]) / matrix[i, i]
        matrix[i + j + 1] -= (matrix[i] * fact)  # Elimination
        li[i + j + 1, i] = fact  # Generating Li
    return matrix, li


def u_solve(matrix, mat_len, solutions):  # Back substitution
    for i in range(mat_len):
        sum = 0
        for j in range(i):
            sum += (matrix[mat_len - i - 1, mat_len - j - 1]) * solutions[mat_len - j - 1]
        solutions[mat_len - i - 1] = (matrix[mat_len - i - 1, -1] - sum) / matrix[mat_len - i - 1, mat_len - i - 1]

    return solutions


def l_solve(matrix, mat_len, solutions):


def lu_decompose(matrix, y):
    mat_len = len(matrix)
    ptot = np.identity(mat_len)  # Initializing Ptot
    ltot = np.identity(mat_len)  # Initializing Ltot
    for i in range(mat_len):
        pivote_pi(matrix, i, mat_len)
        ptot = np.matmul(ptot, pi)
        eliminate_li(matrix, i, mat_len)
        ltot = np.matmul(pi, np.matmul(ltot, np.matmul(pi, li)))
    p, l, u = ptot, ltot, matrix
    # Printing outputs
    print("P: ")
    print(p)
    print("L: ")
    print(np.round(l, 10))
    print("U: ")
    print(np.round(u, 10))
    print("Original Matrix (P.L.U): ")
    print(np.matmul(ptot, np.matmul(ltot, matrix)))

    return p, l, u  # Optional, as we're already printing out values


# Matrix input
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

lu_decompose(matrix, y)
