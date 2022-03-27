import numpy as np
# import scipy.integrate


# Function for Trapezoidal Integral
def trap_int(f_x, x_vals):
    h = x_vals[1] - x_vals[0]
    integral = 0
    n = len(f_x)
    for i in range(n):
        if i == 0 or i == n - 1:
            integral += f_x[i]
        else:
            integral += 2 * f_x[i]
    return integral * (h / 2)


# Function for Simpsons Integral
def sim_int(f_x, x_vals):
    h = x_vals[1] - x_vals[0]
    n = len(f_x)
    integral = 0
    for i in range(n):
        if i == 0 or i == n - 1:
            integral += f_x[i]
        elif i % 2 != 0:
            integral += 4 * f_x[i]
        else:
            integral += 2 * f_x[i]
    return integral * (h / 3)


x = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
fx = np.array([1.0, 1.65, 2.723, 4.48, 7.39, 12.18, 20.09, 33.12, 54.60])


while True:
    method = input("\nWhich method ('S' for Simpson's Method, 'T' for Trapezoidal Method and 'BOTH' or 'st' for both): ")
    if method.upper() == "T":
        print(f"\nTrapezoidal method Integral: {round(trap_int(fx, x), 10)} ")
        break
    if method.upper() == "S":
        print(f"\nSimpsons method Integral: {round(sim_int(fx, x), 10)}")
        break
    if method.upper() == "BOTH" or 'st':
        print(f"\nSimpsons method Integral: {round(sim_int(fx, x), 10)}")
        print(f"Trapezoidal method Integral: {round(trap_int(fx, x), 10)} \n")
        break


# Scipy results for verification (Commented out, in case scipy module is not installed)

# print("*****    SciPy Results   *****")
# print(f"Simpsons method Integral: {round(scipy.integrate.simpson(fx, x), 10)}")
# print(f"Trapezoidal method Integral: {round(scipy.integrate.trapz(fx, x), 10)}")
