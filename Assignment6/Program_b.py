"""Find the value of f(2.5) by quadratic interpolation using the Newton’s divided
difference method. Where, f(0) = 1, f(1) = 3 and f(3) = 55"""

x = 2.5
function_values = {0: 1, 1: 3, 3: 55}
x1, x2, x3 = function_values.keys()

s1 = (function_values[x2] - function_values[x1]) / (x2 - x1)
s2 = (function_values[x3] - function_values[x2]) / (x3 - x2)

if x in function_values.keys():
    print(f'Value at x = {x} : {function_values[int(x)]}')
else:
    output = function_values[x1] + s1 * (x - x1) + ((s2 - s1) / (x3 - x1)) * (x - x1) * (x - x2)
    print(f'Value at x = {x} : {output}')
