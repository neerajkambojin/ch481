n = int(input("Number:"))
prime_numbers = []
i = 2

while True:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)
    if len(prime_numbers) == n:
        break
    else:
        i += 1

print(prime_numbers)

