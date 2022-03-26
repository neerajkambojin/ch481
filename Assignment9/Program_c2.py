# Program c alternative

import numpy as np


# Function for Trapezoidal Integral
def trap_int(f_x, h_val):
    integral = 0
    n = len(f_x)
    for i in range(n):
        if i == 0 or i == n - 1:
            integral += f_x[i]
        else:
            integral += 2 * f_x[i]
    return integral * (h_val / 2)


# Function for Simpsons Integral
def sim_int(f_x, h_val):
    n = len(f_x)
    integral = 0
    for i in range(n):
        if i == 0 or i == n - 1:
            integral += f_x[i]
        elif i % 2 != 0:
            integral += 4 * f_x[i]
        else:
            integral += 2 * f_x[i]

    return integral * (h_val / 3)


a = 0
b = 10


def h_val(a_val, b_val):
    n_val = b_val - a_val + 1
    h_val = (b_val - a_val) / (n_val - 1)
    f_x = np.empty(0)
    x = a_val
    for i in range(n_val):
        val = np.exp(-x) * np.sin(20 * x)
        f_x = np.append(f_x, val)
        x += h_val
    while trap_int(f_x, h_val) < 0.99 * sim_int(f_x, h_val) or trap_int(f_x, h_val) > 1.01 * sim_int(f_x, h_val):
        n_val += 1
        h_val = (b_val - a_val) / (n_val - 1)
        f_x = np.empty(0)
        x = a_val
        for i in range(n_val):
            val = np.exp(-x) * np.sin(20 * x)
            f_x = np.append(f_x, val)
            x += h_val
    print(trap_int(f_x, h_val))
    print(sim_int(f_x, h_val))


h_val(a, b)