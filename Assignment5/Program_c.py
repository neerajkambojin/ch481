# The drunk particle
import numpy as np; import matplotlib.pyplot as plt

x0 = 0

ind_steps = [x0]
means = []
avg_square = []
for time in range(1000):
    a = np.random.uniform(-5,5)
    x0 += a
    ind_steps.append(x0)
    avg_square = np.square(ind_steps)/len(ind_steps)
    mean = np.mean(ind_steps)
    means.append(mean)

plt.plot(means, 'g')
plt.plot(ind_steps, 'r')
plt.plot(avg_square, 'y')
plt.show()

print(means)
