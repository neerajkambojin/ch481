import math

def maxPrimeFactor(n):
   # number must be even
   while n % 2 == 0:
      max_Prime = 2
      n /= 1
   # number must be odd
   for i in range(3, int(math.sqrt(n)) + 1, 2):
      while n % i == 0:
         max_Prime = i
         n = n / i
   # prime number greater than two
   if n > 2:
      max_Prime = n
   return int(max_Prime)
# Driver code to test above function
n = 600851475143
print(maxPrimeFactor(n))