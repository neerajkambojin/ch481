# f(x) = e^(-x) + 4x^3 - 5 = 0, x1 = 1 and x2 = 2
import numpy as np

x1 = 1
x2 = 2

tol_limit = 10 ** (-6)


def fun(x):
    return np.exp(-x) + (4 * (x ** 3)) - 5


while abs(x1 - x2) / 2 >= tol_limit:
    x3 = (x1 + x2) / 2
    if fun(x1) * fun(x3) == 0 or fun(x2) * fun(x3) == 0:
        break
    if fun(x1) * fun(x3) <= 0:
        x2 = x3
    else:
        x1 = x3

print(x3)
print(fun(x3))
