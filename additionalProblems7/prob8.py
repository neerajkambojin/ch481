import numpy as np

print("For matrix A: ")
row_count = int(input("Number of rows: "))
col_count = int(input("Number of column: "))
matrix_a = np.empty((row_count, col_count))
for i in range(row_count):
    for j in range(col_count):
        matrix_a[i, j] = float(input(f"A{i + 1}{j + 1}: "))

print("For matrix B: ")
row_count = int(input("Number of rows: "))
col_count = int(input("Number of column: "))
matrix_b = np.empty((row_count, col_count))
for i in range(row_count):
    for j in range(col_count):
        matrix_b[i, j] = float(input(f"A{i + 1}{j + 1}: "))


def mat_mul(mat_a, mat_b):
    if np.shape(mat_a)[1] != np.shape(mat_b)[0]:
        print("Multiplication not possible!!")
    else:
        mat_c = np.empty((np.shape(mat_a)[0], np.shape(mat_b)[1]))
        for i in range(np.shape(mat_a)[0]):
            for j in range(np.shape(mat_a)[0]):
                mat_c[i, j] = np.sum(mat_a[i]*mat_b[:, j])
        return mat_c


print(mat_mul(matrix_a, matrix_b))
