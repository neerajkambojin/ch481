# Fibo series

def fibo_series(i):  # Defining recursive function for generating Fibonacci series
    if i <= 1:
        return i
    else:
        return fibo_series(i - 1) + fibo_series(i - 2)


series_list = []
number = int(input("Number of terms: "))
for i in range(15):
    print(fibo_series(i))
    series_list.append(fibo_series(i))

for element in series_list:
    if element % 2 != 0:
        print(element)
