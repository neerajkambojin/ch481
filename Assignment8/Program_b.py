# M = P.L.U
import numpy as np
import random


def pivote_pi(mat, i_val, ml):  # Function for pivoting and generating permutation matrix Pi
    global pi
    pi = np.identity(ml)  # Initializing Pi
    for j_val in range(ml - i_val):
        if abs(mat[j_val + i_val, i_val]) == max(abs(mat[i_val:, i_val])):  # Finding row containing the largest element
            mat[[i_val, j_val + i_val]] = mat[[j_val + i_val, i_val]]  # Pivoting
            pi[[i_val, j_val + i_val]] = pi[[j_val + i_val, i_val]]  # Generating Pi
    return mat, pi


def eliminate_li(mat, i_val, ml):  # For elimination and Li
    global li
    li = np.identity(ml)  # Initializing Li
    for j_val in range(ml - i_val - 1):
        fact = (mat[i_val + j_val + 1, i_val]) / mat[i_val, i_val]
        mat[i_val + j_val + 1] -= (mat[i_val] * fact)  # Elimination
        li[i_val + j_val + 1, i_val] = fact  # Generating Li
    return mat, li


def lu_decompose(mat):
    ml = len(mat)
    ptot = np.identity(ml)  # Initializing Ptot
    ltot = np.identity(ml)  # Initializing Ltot
    for i_val in range(ml):
        pivote_pi(mat, i_val, ml)
        ptot = np.matmul(ptot, pi)
        eliminate_li(mat, i_val, ml)
        ltot = np.matmul(pi, np.matmul(ltot, np.matmul(pi, li)))
    p, l, u = ptot, ltot, mat
    # Printing outputs
    print("P: ")
    print(p)
    print("L: ")
    print(np.round(l, 10))
    print("U: ")
    print(np.round(u, 10))
    print("Original Matrix (P.L.U): ")
    print(np.matmul(ptot, np.matmul(ltot, mat)))
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
