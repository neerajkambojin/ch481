import numpy as np #Importing numpy

#Generating matrix A
matrix_A = np.array([[5,3,9,4,2,0],
                     [8,3,4,-1,5,1],
                     [0,2,4,-2,8,5]])

new_matrix = np.empty((0,6),int) #Generating empty matrix
for row in matrix_A:
    row = sorted(row, reverse=True) #Sorting rows
    new_matrix = np.vstack((new_matrix, row)) # Adding sorted rows to new matrix

print('Rearranged matrix is:')
print(new_matrix) #Printing matrix with sorted rows