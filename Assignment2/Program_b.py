# To calculate average height and standard deviation

import math #Importing math module

heights = [4.5, 4.9, 4.8, 5.3, 5.7, 5.0, 4.8, 5.2, 4.7, 5.1, 4.4, 4.9] # Making list of heights

count = len(heights) # Counting number of students

total = sum(heights) # Sum of heights

average_height = total/count # Calculating average height

print(f'\nThe average height is {average_height}\n') # Printing average height

sum = 0

#Calculation of standard deviation

for height in heights:

    difference = (height - average_height)**2

    sum += difference

std = math.sqrt(sum/count)

print(f'The standard deviation is {std}') # Printing standard deviation
