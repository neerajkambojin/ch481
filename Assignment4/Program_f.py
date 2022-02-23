import numpy as np
import matplotlib.pyplot as plt  # Importing numpy and pyplot modules

mean = 5
std_dev = 1  # Setting mean and standard deviation values
hist1 = np.random.normal(mean, std_dev, 1000)  # Creating first normal distribution
hist2 = np.random.normal(mean, std_dev, 100000)  # Creating 2nd normal distribution

plt.hist(hist1, alpha=0.7, edgecolor='green', density=True, stacked=True, label='Histogram 1')  # Making 1st histogram
plt.hist(hist2, alpha=0.3, edgecolor='red', density=True, stacked=True, label='Histogram 2')  # Making 2nd histogram

# Giving labels to axes
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper left')  # Legend location
plt.title('Histograms')  # Title

# Printing the histograms
plt.show()
