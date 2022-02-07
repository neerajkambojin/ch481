import numpy as np  # Importing numpy

# Generating matrix E
matrix_E = np.array([[5, 9, -2],
                     [8, 4, 7],
                     [3, 8, 8]])

# Generating matrix F
matrix_F = np.array([[3, 6, 4],
                     [-2, 6, 3],
                     [1, 5, 2]])

# Subtracting matrix E from matrix F to get matrix D
matrix_D = matrix_F - matrix_E

# Printing the transpose of resultant matrix D
print('The transpose of matrix D is:')
print(np.transpose(matrix_D))
