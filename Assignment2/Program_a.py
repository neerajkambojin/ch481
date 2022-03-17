# To find out the sum of individual digits of a 5-digit number

the_number = input('Enter 5 digit number: ')  # Asking for input
total = int(the_number[0]) + int(the_number[1]) + int(the_number[2]) + int(the_number[3]) + int(
    the_number[4])  # Adding the digits
print(f'The sum of the individual digits of given number is {total}')  # Printing the sum

# Alternative

the_number = input('Enter 5 digit number: ')  # Asking for input

while len(the_number) != 5:  # To ensure that the given number is 5 digit only
    print('Please enter a 5 digit number only.')
    the_number = input('Enter the 5 number: ')

total = 0

for digit in the_number:  # Adding up digits
    total += int(digit)

print(f'The sum of the individual digits of given number is {total}')  # Printing the sum
