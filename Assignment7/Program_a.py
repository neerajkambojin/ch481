# Estimate pi

"""in range(10000):
generate random pairs #np.random.uniform

in random pairs:
count pairs with length <= 1 # because circle radius is 1

probability = (pairs with length <= 1)/total pairs
pi = probability * 4 # because probability = pi/4
"""

import numpy as np

i = 0
n = int(input("How many pairs: "))

# Generating 10000 pairs of uniform random distribution b/w -1 and +1
for j in range(n):
    x = np.random.uniform(-1, 1, 2)
    if np.sum(np.square(x)) <= 1:  # No need to sqrt because for number less than or equal to 1 will have sqrt <= 1
        i += 1

prob = i / n
print(f"Probability : {prob}")
print(f"Value of pi : {prob * 4}")  # From given formula
