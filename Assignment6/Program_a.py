# Linear interpolation using newtons's divided difference method

function_values = {0.1 : 1.4, 0.2 : 1.56, 0.3 : 1.76, 0.4 : 2.0, 0.5 : 2.28}

x = float(input('Enter the number: '))
x1 = 0
x2 = 0
for i in function_values:
    if i < x and x-i < x - x1:
        x1 = i
for i in function_values:
    if i > x and i - x < i - x1:
        x2 = i
print(x1,x2)
slope = (function_values[x2]-function_values[x1])/(x2-x1)

equation = function_values[x1] + slope*(x - x1)
print(equation)