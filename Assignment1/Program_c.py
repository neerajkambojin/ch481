# Program to find the sum of x and y

import math # Importing math module

z = float(input('Give value of z: ')) # Input z value

w = float(input('Give value of w: ')) # Input w value

x = math.exp(z) + math.cos(math.pi/2) + math.pow(z, 3)*math.sqrt(w) # Equation for x

y = 2*(math.sqrt(z*w)) + z/w + math.fabs(math.acos(-1)) # Equation for y

print(f'The value of x + y is {x+y}') # Output
