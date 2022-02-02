number = float(input('Number: '))

if number == 0:
    print('It is zero')

if number > 0:
    if number%2 == 0:
        print('Positive even number')
    else:
        print('Positive odd number')

if number < 0:
    if number%2 == 0:
        print('Negative even number')
    else:
        print('Negative odd number')

