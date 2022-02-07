# Heights

import math  # Importing math module

with open('heights.txt') as heights:  # Opening student_heights.txt file in read mode
    heights_list = [float(height[-4:-1]) for height in heights]  # Making list of heights

sum_of_heights = 0
count_of_heights = len(heights_list)  # Counting number of students

for height in heights_list:  # Sum of heights
    sum_of_heights += height

average_height = sum_of_heights / count_of_heights  # Calculating average height
print(f'The average height is {average_height} ft.')  # Printing average height

# Calculation of standard deviation
sum = 0

for height in heights_list:
    difference = (height - average_height) ** 2
    sum += difference

std = math.sqrt(sum / count_of_heights)
print(f'The standard deviation is {std}')  # Printing standard deviation
