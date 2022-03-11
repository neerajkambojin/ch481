import numpy as np

mat_len = int(input("Order of matrix: "))
matrix = np.empty((mat_len, mat_len))
y = np.empty((mat_len, 1))
for i in range(mat_len):
    for j in range(mat_len):
        matrix[i, j] = float(input(f"A{i + 1}{j + 1}: "))

print(matrix)

def diag_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i, i]
    return sum

print(diag_sum(matrix))