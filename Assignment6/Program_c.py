import numpy as np

matrix = np.array([[0, 2, 0, 1, 0],
                   [2, 2, 3, 2, -2],
                   [4, -3, 0, 1, -7],
                   [6, 1, -6, -5, 6]], float)

mat_len = len(matrix[:, 0])

# Iterations:
for i in range(mat_len):
    where = np.where(abs(matrix[i:, i]) == max(abs(matrix[i:, i])))
    where = where[0][0] + i
    matrix[[i, where]] = matrix[[where, i]]
    for j in range(i + 1, 4):
        if matrix[j][i] != 0:
            matrix[j] = (matrix[j] * matrix[i][i]) / (matrix[j][i])
            if matrix[j][i] - matrix[i][i] == 0:
                matrix[j] = matrix[j] - matrix[i]
            else:
                matrix[j] = matrix[j] - matrix[i]

value = [0, 0, 0, 0]  # Initializing x values
# Solving for x values:
for i in range(mat_len):
    value[3 - i] = (matrix[3 - i][-1] - (
            matrix[3 - i][-2] * value[3] + matrix[3 - i][-3] * value[2] + matrix[3 - i][-4] * value[1])) / \
                   matrix[3 - i][-2 - i]
# Printing x values:
for i in range(4):
    print(f'x{i + 1} = {value[i]}')
