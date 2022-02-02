number = input('Give the number: ') #1234

reverse = ''

for digit in number:
    reverse = digit + reverse

print(f'The reverse of the number is {reverse}.') #4321

