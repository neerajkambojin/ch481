import math


def fun(x, n):
    if n == 0:
        return 1
    else:
        return (pow(x, n) / math.factorial(n)) + fun(x, n - 1)


print(fun(5, 2))
