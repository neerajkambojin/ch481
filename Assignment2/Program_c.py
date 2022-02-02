# Marks

marks = [41,49,57,62,75,55,52,82,77,67,61,48] # Making list of marks

print(f'The highest marks are {max(marks)}.\n') # Printing highest marks

print(f'The lowest marks are {min(marks)}.\n') # Printing lowest marks

marks.sort() # Sorting list

print(f'The sorted list of marks in ascending order is:\n{marks}\n') # Printing list in ascending order

marks.reverse() # Reversing list

print(f'The sorted list of marks in descending order is:\n{marks}\n') # Printing list in descending order

top5 = marks[0:5] # Slicing list to get top 5 marks

average = sum(top5)/len(top5) # Calculating average of top marks

print(f'The average of top 5 is {average}') # Printing average of top 5 marks
