# M = P.L.U
import random
import numpy as np


def pivote_pi(mat, i_val, ml):
    global pi, swap
    pi = np.identity(ml)  # Initializing Pi
    for j_val in range(ml - i_val):
        if abs(mat[j_val + i_val, i_val]) == max(abs(mat[i_val:, i_val])):  # Finding row containing the largest element
            mat[[i_val, j_val + i_val]] = mat[[j_val + i_val, i_val]]  # Pivoting
            if j_val + i_val != i_val:  # To count number of swaps
                swap = 1
            else:
                swap = 0
            pi[[i_val, j_val + i_val]] = pi[[j_val + i_val, i_val]]
            break
    return mat, pi, swap


def eliminate_li(mat, i_val, ml):
    global li
    li = np.identity(ml)  # Initializing Pi
    for j_val in range(ml - i_val - 1):
        fact = (mat[i_val + j_val + 1, i_val]) / mat[i_val, i_val]
        mat[i_val + j_val + 1] -= (mat[i_val] * fact)  # Elimination
        li[i_val + j_val + 1, i_val] = fact  # Generating Li
    return mat, li


def lu_det(mat):
    print("\nMatrix: ")
    print(mat)
    ml = len(mat)
    ptot = np.identity(ml)
    ltot = np.identity(ml)
    count = 0
    for i_val in range(ml):
        pivote_pi(mat, i_val, ml)
        count += swap
        ptot = np.matmul(ptot, pi)
        eliminate_li(mat, i_val, ml)
        ltot = np.matmul(pi, np.matmul(ltot, np.matmul(pi, li)))
    p, u = ptot, mat
    det_p = np.power(-1, count)
    det_u = np.prod(np.diag(u))  # l not required as its diagonal contains 1s and hence its det = 1
    print(f"\nDeterminant: {round(det_u * det_p, 10)}")


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

lu_det(matrix)
