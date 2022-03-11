import numpy as np

mat_len = int(input("Order of matrix: "))
matrix = np.empty((mat_len, mat_len))
y = np.empty((mat_len, 1))
for i in range(mat_len):
    for j in range(mat_len):
        matrix[i, j] = float(input(f"A{i + 1}{j + 1}: "))

print(matrix)

n = int(input("N: "))


def row_ret(matrix, n):
    mat_c = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            mat_c[i, j] = matrix[i, j]

    print("The required matrix is: ")
    return mat_c


print(row_ret(matrix, n))