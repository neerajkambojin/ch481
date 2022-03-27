import numpy as np


# Trapezoidal integral function
def trap_int(ff, hh):
    integral = 0
    n = len(ff)
    for i in range(n):
        if i == 0 or i == n - 1:
            integral += ff[i]
        else:
            integral += 2 * ff[i]
    return (hh / 2) * integral


# Simpsons integral method
def simpsons(ff, hh):
    n = len(ff)
    integral = 0
    for i in range(n):
        if i == 0 or i == n - 1:
            integral += ff[i]
        elif i % 2 == 0:
            integral += 2 * ff[i]
        else:
            integral += 4 * ff[i]
    return (hh / 3) * integral


# Function for finding h
def det_h(a, b):
    n = b - a + 1
    hh = (b - a) / (n - 1)
    ff = np.empty(n)
    x = a

    # Making array
    for i in range(n):
        fx = np.exp(-x) * np.sin(20 * x)
        ff[i] = fx
        x += hh
    # Condition
    while trap_int(ff, hh) < 0.99 * simpsons(ff, hh) or trap_int(ff, hh) > 1.01 * simpsons(ff, hh):
        n += 2  # So that number of terms remail odd
        hh = (b - a) / (n - 1)
        ff = np.empty(n)
        x = a
        for i in range(n):
            fx = np.exp(-x) * np.sin(20 * x)
            ff[i] = fx
            x += hh

    # Results
    print()
    print(f"Trapezoidal integral: {trap_int(ff, hh)}")
    print(f"Simpsons integral: {simpsons(ff, hh)}")
    print(f"h: {hh}")
    print(f"Margin: {((simpsons(ff, hh) - trap_int(ff, hh)) / simpsons(ff, hh)) * 100}%")
    return hh


a = 0
b = 10
det_h(a, b)
