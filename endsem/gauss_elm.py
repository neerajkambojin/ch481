# Gaussian Elimination

import numpy as np


def appender(mat, y0):  # Defining functions for appending, pivoting, elimination and back substtution
    mat = np.hstack((mat, y0))  # Appends y values to matrix
    return mat


def pivoter(mat, i_val, ml):
    for j_val in range(ml - i_val):
        if abs(mat[j_val + i_val, i_val]) == max(abs(mat[i_val:, i_val])):  # Finding row containing the largest element
            mat[[i_val, j_val + i_val]] = mat[[j_val + i_val, i_val]]  # Pivoting
    return mat


def eliminator(mat, i_val, ml):
    for j_val in range(ml - i_val - 1):
        mat[i_val + j_val + 1] = mat[i_val + j_val + 1] - (mat[i_val] * mat[i_val + j_val + 1, i_val]) / mat[
            i_val, i_val]  # Elimination
    return mat


def u_solve(mat, ml, solutions):  # Back substitution
    for i_val in range(ml):
        addition = 0
        for j_val in range(i_val):
            addition += (mat[ml - i_val - 1, ml - j_val - 1]) * solutions[ml - j_val - 1]
        solutions[ml - i_val - 1] = (mat[ml - i_val - 1, -1] - addition) / mat[ml - i_val - 1, ml - i_val - 1]

    return solutions


def ge(mat, y0):  # Combining all functions
    ml = len(mat)
    mat = appender(mat, y0)

    i_val = 0
    while i_val < ml:
        mat = pivoter(mat, i_val, ml)
        mat = eliminator(mat, i_val, ml)
        i_val += 1

    solutions = np.zeros(ml)
    solutions = u_solve(mat, ml, solutions)

    return solutions