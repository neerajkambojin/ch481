import numpy as np
import matplotlib.pyplot as plt  # Importing numpy and pyplot modules


def fibo_series(step):  # Defining recursive function for generating Fibonacci series
    if step <= 1:
        return step
    else:
        return fibo_series(step - 1) + fibo_series(step - 2)


number = 14

series = np.array([])

for i in range(number):
    series = np.append(series, fibo_series(i))  # Generating Fibonacci series of 14 numbers and appending it to array

print('Fibonacci series:')
print(series)  # Printing the array

plt.plot(series, 'go:', label='Fibonacci Series')  # Ploting the series

# Labelling the axes
plt.xlabel('Numbers')
plt.ylabel('Values')
plt.legend(loc='upper left')  # Defining legend location
plt.title('Fibonacci Series')
plt.savefig('Program_e_output.pdf')  # Saving output to pdf file
plt.show()  # Showing plot
