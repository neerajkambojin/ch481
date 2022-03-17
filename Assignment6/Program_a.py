def range_detector(function):
    x_values = list(function.keys())
    x_values.sort()
    low, high = None, None
    if x > x_values[-1]:
        low, high = x_values[-2:]
    elif x < x_values[0]:
        low, high = x_values[:2]
    else:
        for i in x_values:
            if i <= x:
                low = i
        for i in x_values:
            if i >= x:
                high = i
                break
    return low, high


def interpolation(x_0, x_1, x_2):
    print(f'x1 = {x_1}, x2 = {x_2}')
    if x_0 in function_values.keys():
        print(f'Value at x = {x_0} : {function_values[x_0]}')
    else:
        slope = (function_values[x_2] - function_values[x_1]) / (x_2 - x_1)
        output = function_values[x_1] + slope * (x_0 - x_1)
        print(f'Value at x = {x_0} : {output}')


function_values = {0.1: 1.4, 0.2: 1.56, 0.3: 1.76, 0.4: 2.0, 0.5: 2.28}
x = float(input('Enter x: '))
x1, x2 = range_detector(function_values)
interpolation(x, x1, x2)
