# The drunk particle
import numpy as np; import matplotlib.pyplot as plt

x0 = 0 # Initial position

ind_steps = [x0] #Individual steps
means = [] # Initialising average values
avg_square = [] # Initialising square average values

# Simulating trajectory 1000 times
for time in range(1, 1001):
    a = np.random.uniform(-5,5)
    x0 += a
    ind_steps.append(x0)
    avg_square = np.square(ind_steps)/len(ind_steps)
    mean = np.mean(ind_steps)
    means.append(mean)

# Plots
plt.plot(means, 'g--', label = 'Mean')
plt.plot(avg_square, 'y', label = 'Square Mean')
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
plt.title("Plots for positions of 'Drunk' particle")
plt.show()
