# Matrix multiplication
import numpy as np #Importing numpy module

# Generating matrix A
matrix_A = np.array([[5,9,-2],
                     [8,4,5],
                     [0,4,8]])

# Generating matrix B
matrix_B = np.array([[8,4],
                     [0,5],
                     [5,2]])

#Matrix multiplication
matrix_C = np.matmul(matrix_A,matrix_B)

#Printing resultant matrix
print('The product of matrix A and B is:')
print(matrix_C)