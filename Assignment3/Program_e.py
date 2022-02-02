# To find factorial

n = int(input('Enter the number: ')) # Asking for number

fact = 1

for i in range(1, n +1):
    fact *= i               #Calculating factorial of number

print(fact) # Printing the factorial