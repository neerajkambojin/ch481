# To find the largest number among three numbers.

# Asking for 3 numbers
num1 = float(input('Enter 1st number: '))
num2 = float(input('Enter 2nd number: '))
num3 = float(input('Enter 3rd number: '))

# Finding out the largest number
largest_number = num1

if num2 > largest_number:
    largest_number = num2
if num3 > largest_number:
    largest_number = num3

# Printing largest number
print(f'The largest number among these three is {largest_number}.')
