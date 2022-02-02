import numpy as np ; import matplotlib.pyplot as plt


mean = 5; std_dev = 1
hist1 = np.random.normal(mean, std_dev, 1000)
hist2 = np.random.normal(mean, std_dev, 100000)

plt.hist(hist1)
plt.show()
plt.hist(hist2)
plt.show()