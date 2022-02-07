# Calculation of area of triangle

import math  # Importing math module

side_a = 3  # Side 'a' of triangle in cm.

side_b = 4  # Side 'b' of triangle in cm.

side_c = 5  # Side 'c' of triangle in cm.

s = (side_a + side_b + side_c) / 2  # Calculation of semi perimeter of triangle.

area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))  # Calculation of area

print(f'The area of the triangle is {area} cm²')  # Printing area of triangle
