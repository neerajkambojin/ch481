# Finding roots of polynomial

import numpy as np

x1 = 1
x2 = 2
tol_limit = 10 ** (-6)
iterative_values = []


def fun(x):
    return np.exp(-x) + (4 * (x ** 3)) - 5  # Function for calculating value of polynomial for given x


x3 = None
while abs(x1 - x2) >= 2 * tol_limit:  # Setting tolerance limit
    x3 = (x1 + x2) / 2
    iterative_values.append(x3)
    if fun(x3) == 0:
        break
    elif fun(x1) * fun(x3) <= 0:
        x2 = x3
    else:
        x1 = x3

# Printing out root
print(f'Root: {x3}')
print('The iterative values are:')
print(iterative_values)
print(f'{len(iterative_values)} iterations.')
