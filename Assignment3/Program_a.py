# Heights
from Assignment2.Program_b import mean_n_std

with open('heights.txt') as heights:  # Opening student_heights.txt file in read mode
    heights_list = [float(height.split(":")[-1]) for height in heights]  # Making list of heights

print(f"Mean, Standard Deviation: {mean_n_std(heights_list)}")
