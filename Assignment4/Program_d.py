import numpy as np  # Importing numpy

array_A = np.array([32, 45, 23, 32, 34, 45, 32, 54, 56, 76, 23])  # Creating first 1 - Dimensional array
array_B = np.array([56, 44, 33, 87, 13, 97, 48, 37, 93, 37, 52])  # Creating second 1 - Dimensional array

new_row = []
index = 0

# Arranging elements of both arrays in required fashion.
for i in array_A:
    new_row.append(i)
    new_row.append(array_B[index])
    index += 1

# Making array of rearranged elements
array_C = np.array(new_row)

# Printing out the resultant array
print('Merged array is:')
print(array_C)
