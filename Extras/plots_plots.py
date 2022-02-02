from matplotlib import pyplot; import numpy as np

x_values = np.linspace(1, 20, 20)
y1_values = x_values**2
y2_values = x_values**2.1
# pyplot.semilogy(x_values,y_values, 'go-', linewidth = 1.5, markersize = 4, label = 'Squares')
# pyplot.show()

pyplot.plot(x_values,y1_values,x_values,y2_values,'go-', linewidth = 1.5, markersize = 4, label = 'Y1')
pyplot.legend(loc = 'upper left')
pyplot.axis([0,22,0,500])
pyplot.show()