"""This program finds the maximum value of h for which the results from both methods are within 1%.
If we only have to find h, for which results are within 1%, the increment in n (Line 54) can be increased
to make the code faster but the resulting h value will not be the maximum for which the results are within 1%."""

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


def h_val(a_val, b_val):
    n_val = b_val - a_val + 1
    while True:
        h_val = (b_val - a_val) / (n_val - 1)
        f_x = np.empty(0)
        x = a_val
        for i in range(n_val):
            val = np.exp(-x) * np.sin(20 * x)
            f_x = np.append(f_x, val)
            x += h_val
        if 0.99 * sim_int(f_x, h_val) < trap_int(f_x, h_val) < 1.01 * sim_int(f_x, h_val):
            s_int = (sim_int(f_x, h_val))
            t_int = (trap_int(f_x, h_val))
            print(f"h value: {h_val}")
            print(f"Number of terms: {n_val}")
            print(f"Simpsons method Integral: {s_int}")
            print(f"Trapezoidal method Integral: {t_int}")
            print(f"Difference: {round(((s_int - t_int) / s_int) * 100, 5)}% of Simpsons method Integral.")
            return h_val
        else:
            n_val += 1  # This increment can be changed to 10, 50, 100 or any bigger values to make the code faster.


a, b = 0, 10

h_val(a, b)
