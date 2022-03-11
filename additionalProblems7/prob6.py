import numpy as np

mat_len = int(input("Order of matrix: "))
matrix = np.empty((mat_len, mat_len))
y = np.empty((mat_len, 1))
for i in range(mat_len):
    for j in range(mat_len):
        matrix[i, j] = float(input(f"A{i + 1}{j + 1}: "))

print(matrix)


def is_daig(matrix):
    mat_len = len(matrix)
    for i in range(mat_len):
        for j in range(mat_len):
            if j != i:
                if matrix[i, j] != 0:
                    print("Not a diagonal matrix!!")
                    break
                else:
                    print("Diagonal matrix!!")


is_daig(matrix)