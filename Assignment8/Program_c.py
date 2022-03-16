# M = P.L.U
import random
import numpy as np


def pivote_pi(matrix, i, mat_len):
    global pi, swap
    pi = np.identity(mat_len)  # Initializing Pi
    for j in range(mat_len - i):
        if abs(matrix[j + i, i]) == max(abs(matrix[i:, i])):  # Finding row containing the largest element
            matrix[[i, j + i]] = matrix[[j + i, i]]  # Pivoting
            if j + i != i:  # To count number of swaps
                swap = 1
            else:
                swap = 0
            pi[[i, j + i]] = pi[[j + i, i]]
            break
    return matrix, pi, swap


def eliminate_li(matrix, i, mat_len):
    global li
    li = np.identity(mat_len)  # Initializing Pi
    for j in range(mat_len - i - 1):
        fact = (matrix[i + j + 1, i]) / matrix[i, i]
        matrix[i + j + 1] -= (matrix[i] * fact)  # Elimination
        li[i + j + 1, i] = fact  # Generating Li
    return matrix, li


def lu_det(matrix):
    print("\nMatrix: ")
    print(matrix)
    mat_len = len(matrix)
    ptot = np.identity(mat_len)
    ltot = np.identity(mat_len)
    count = 0
    for i in range(mat_len):
        pivote_pi(matrix, i, mat_len)
        count += swap
        ptot = np.matmul(ptot, pi)
        eliminate_li(matrix, i, mat_len)
        ltot = np.matmul(pi, np.matmul(ltot, np.matmul(pi, li)))
    p, u = ptot, matrix
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
