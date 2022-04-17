# 600851475143

import time

start_time = time.time()

number = 600851475143

for i in range(2, number):
    if number % i == 0:
        q = int(number / i)
        for j in range(2, q):
            if int(q % j) == 0:
                break
        else:
            print(q)
            break

print('Time elapsed : ', format(time.time() - start_time))
