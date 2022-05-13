import numpy as np


# Function for finding F coefficient values by divided difference table
def coeff_part(x_vals, f_x):
    n = len(x_vals)
    mat = np.zeros([n, n + 1])
    # x and fx value columns
    mat[:, 0] = x_vals
    mat[:, 1] = f_x
    for j in range(2, n + 1):
        for i in range(n - j + 1):
            mat[i, j] = (mat[i + 1, j - 1] - mat[i, j - 1])/(mat[i + j - 1, 0] - mat[i, 0])
    return mat[0][2:]


# Function to calculate the part including input x
def var_part(x_vals, x_val, i):
    prod = 1
    j = 0
    while j < i + 1:
        prod *= (x_val - x_vals[j])
        j += 1
    summation = 0
    j = 0
    while j < i + 1:
        summation += 1/(x_val - x_vals[j])
        j += 1
    prod *= summation
    return prod


# Combining the functions
def differentiate(x_vals, f_x, x_val):
    total = 0
    cm = coeff_part(x_vals, f_x)
    n = len(x_vals)
    for i in range(n - 1):
        total += cm[i] * var_part(x_vals, x_val, i)
    return total


# x and fx arrays
x_s = np.array([1, 2, 3, 4, 5, 6, 7])
fx = np.array([1, 8, 27, 64, 125, 216, 343])
x = float(input("Find differential at(x): "))

for i in range(len(x_s)):
    if x_s[i] == x:
        soln = fx[i]
        break
else:
    soln = differentiate(x_s, fx, x)

print("The differential value is:", soln)
