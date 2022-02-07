import numpy as np

x1 = float(input('x0: '))
x2 = float(input('x1: '))
tol_limit = float(input('Enter tolerance limit: '))
roots = []


# Function to return f(x) value
def root(x):
    return x * np.sin(x)


# Roots
while abs(x1 - x2) > tol_limit:
    if root(x1) * root(x1 + tol_limit) < 0:
        roots.append(x1)
    x1 += tol_limit

# Printing roots
print(f'The roots are: {roots}')
