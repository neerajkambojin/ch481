# Trapezoidal Rule

x = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]
fx = [0, 0.203, 0.423, 0.684, 1.03, 1.557, 2.572]

def trap_int(f_x, x_vals):
    h = x_vals[1] - x_vals[0]
    integral = 0
    n = len(f_x)
    for i in range(n):
        if i == 0 | i == n - 1:
            integral += f_x[i]
        else:
            integral += 2*f_x[i]
    return integral * (h/2)

print(f"Integral: {trap_int(fx, x)}")
