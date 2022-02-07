# The drunk particle
import numpy as np
import matplotlib.pyplot as plt

x0 = 0  # Initial position

ind_steps = [x0]  # Individual steps
means = []  # Initialising average values
squares_avg = []  # Initialising square average values
mean_squares = []

# Simulating trajectory 1000 times
for time in range(1, 1001):
    a = np.random.uniform(-5, 5)
    x0 += a
    ind_steps.append(x0)
    mean = np.mean(ind_steps)
    means.append(mean)
    rms = np.sqrt(np.sum(np.square(ind_steps)) / len(ind_steps))
    squares_avg.append(rms)
    mean_square = np.sum(np.square(ind_steps)) / len(ind_steps)
    mean_squares.append(mean_square)

# Plots
plt.plot(means, 'g--', label='Mean')
plt.plot(squares_avg, 'y', label='Root mean square')
plt.plot(mean_squares, 'r:', label='Mean Square')
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
plt.title("Plots for positions of 'Drunk' particle")
plt.show()
plt.plot(mean_squares, 'r:', label='Mean Square')
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
plt.show()
