n = 4

count = 1
i = 2
while count <= n:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        count += 1
    i += 1
