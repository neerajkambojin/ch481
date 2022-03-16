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


def lu_decompose(matrix):
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
    mat_len = int(input("Order of matrix (Hit enter to take a random matrix): "))
    print("Enter matrix elements: ")
    matrix = np.empty((mat_len, mat_len))
    for i in range(mat_len):
        for j in range(mat_len):
            matrix[i, j] = float(input(f"A{i + 1}{j + 1}: "))
except ValueError:
    print("\nRandom matrix taken!!!")
    mat_len = random.randint(2, 5)
    matrix = np.empty((mat_len, mat_len))
    for i in range(mat_len):
        for j in range(mat_len):
            matrix[i, j] = random.randint(-10, 10)
    print(matrix)

lu_decompose(matrix)
