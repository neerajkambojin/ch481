# from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from gauss_elm_puspa import *

np.set_printoptions(threshold=np.inf)
def y_value(o_vals, x_0, x):
    y = 0
    for i in range(4):
        y += (o_vals[i] * ((x - x_0) ** (3 - i)))
    return y


def animate(i):
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    x.append(x_vals[i])
    y.append(y_vals[i])

    ax.clear()
    ax.plot(x, y, label='Spline')
    
    ax.set_xlim([98, 302])
    ax.set_ylim([0.12, 1.04])
    ax.plot(xi, yi, 'o:', alpha=0.35, label='From data')
    plt.legend(loc = 'upper left')


with open('spline_dataset.dat') as file:
    xi = []
    yi = []
    while True:
        line = file.readline()
        if line == "":
            break
        xi.append(float(line.split()[0]))
        yi.append(float(line.split()[1]))

xi = np.array(xi)
yi = np.array(yi)
n = (len(yi) - 1)
h = (xi[1] - xi[0])

x_arr = np.zeros([4 * n, 4 * n])

inc = 3
for i in range(n):
    x_arr[i, inc] = 1
    inc = inc + 4

a = 0
b = 4
for k in range(n, 2 * n):
    h_cube = np.power(h, 4)
    for l in range(a, b):
        x_arr[k, l] = h_cube / h
        h_cube /= h
    a = b
    b += 4

a = 0
b = 4
l = a
for k in range(2 * n, (3 * n) - 1):
    nimo = 3 * (h ** 2)
    div = 1
    for l in range(a, b - 1):
        x_arr[k, l] = nimo / div
        if l == a:
            div = 1.5 * h
        else:
            div = 3 * (h ** 2)
    x_arr[k, l + 4] = -1
    a = b
    b += 4

a = 0
b = 4
q = a
for p in range((3 * n) - 1, (4 * n) - 2):
    var = 3 * h
    for q in range(a, b - 2):
        x_arr[p, q] = var
        var = 1
    x_arr[p, q + 4] = -1
    a = b
    b += 4

x_arr[((4 * n) - 2), 0] = 6 * h
x_arr[((4 * n) - 2), 1] = 2
x_arr[((4 * n) - 1), ((4 * n) - 4)] = 6 * h
x_arr[((4 * n) - 1), ((4 * n) - 3)] = 2

y_arr = np.zeros([4 * n, 1])

for m in range(n):
    y_arr[m, 0] = yi[m]
    y_arr[m + n] = yi[m + 1]

sols = Guass_Elimination(x_arr, y_arr)

x_vals = np.empty(0)
y_vals = np.empty(0)

for i in range(n):
    ind = i * 4
    abcd_vals = np.empty(0)
    while ind < (i * 4) + 4:
        abcd_vals = np.append(abcd_vals, sols[ind])
        ind += 1
    xs = np.linspace(xi[i], xi[i + 1], 10)
    ys = np.empty(0)
    for x in xs:
        ys = np.append(ys, y_value(abcd_vals, xi[i], x))
    x_vals = np.append(x_vals, xs)
    y_vals = np.append(y_vals, ys)

x = []
y = []
fig, ax = plt.subplots()

ani = FuncAnimation(fig, animate, frames=200, interval=1, repeat=False)

plt.show()
