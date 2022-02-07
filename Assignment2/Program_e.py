# To calculate roots of quadratic equation

a = float(input('Enter coefficient of x²: '))  # Asking for coefficient of x².

b = float(input('Enter coefficient of x: '))  # Asking for coefficient of x.

c = float(input('Enter constant term: '))  # Asking for constant term.

d_sqrt_value = (b ** 2 - 4 * a * c) ** 0.5  # Calculating value of square root of Discriminant.

root1 = (-b + d_sqrt_value) / (2 * a)  # Calculating 1st root.

root2 = (-b - d_sqrt_value) / (2 * a)  # Calculating 2nd root.

print(f'The roots of given quadratic equation are: {root1} and {root2}.')  # Printing out roots.
