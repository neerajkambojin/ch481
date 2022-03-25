print("Hello World!!!")



def step_size(f_x, a, b):
    # Function for Trapezoidal Integral
    def trap_int(f_x, h):
        integral = 0
        n = len(f_x)
        for i in range(n):
            if i == 0 or i == n - 1:
                integral += f_x[i]
            else:
                integral += 2 * f_x[i]
        return integral * (h / 2)

    # Function for Simpsons Integral
    def sim_int(f_x, h):
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

    d = 1
    h = (b - a)/d
    while trap_int(f_x, h) < 0.99 * sim_int(f_x, h) or trap_int(f_x, h) > 1.01 * sim_int(f_x, h):
        d += 1
    print(h)


def trap_int(f_x, x_vals):
    pass