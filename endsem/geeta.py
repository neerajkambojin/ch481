import numpy as np
import matplotlib.pyplot as plt
from gauss_elm import *


def y_value(abcd, x0, x):
    y = 0
    for i in range(4):
        y += (abcd[i] * ((x - x0)**(3-i)))
    return y


xi = np.linspace(100, 300, 21)
# xi = [1,2,3,4]

yi = [0.429798, 0.352640, 0.289338, 0.237408, 0.194852, 0.160559, 0.164582, 0.273047, 0.483905, 0.724760, 0.908118,
      0.992072, 0.979871, 0.900932, 0.790204, 0.671060, 0.548327, 0.414375, 0.307015, 0.251896, 0.206746]
# yi = [5,6,7,8]
n = len(yi) - 1
h = xi[1] - xi[0]
mat = np.zeros([4 * n, 4 * n], float)

for i in range(n):
    mat[i, (4*i) + 3] = 1


l = 0
m = l + 4
for k in range(n, 2*n):
    dino = 1
    m = l + 4
    while l < m:
        mat[k, l] = (h**3) / dino
        dino *= h
        l += 1

m = 0
for k in range(2 * n, 3 * n - 1):
    nimo = 3 * (h ** 2)
    div = 1
    for l in range(4*m, 4*(m + 1) - 1):
        mat[k, l] = nimo / div
        if l == 4*m:
            div = 1.5 * h
        else:
            div = 3 * (h ** 2)
    mat[k, l + 4] = -1
    m += 1

m = 0
for k in range((3 * n) - 1, (4 * n) - 2):
    nimo = 3 * h
    for l in range(4 * m, 4 * (m + 1) - 2):
        mat[k, l] = nimo
        nimo = 1
    mat[k, l + 4] = -1
    m += 1


mat[((4 * n) - 2), 0] = (6 * h)
mat[((4 * n) - 2), 1] = 2
mat[((4 * n) - 1), ((4 * n) - 4)] = (6 * h)
mat[((4 * n) - 1), ((4 * n) - 3)] = 2

# print(mat)
# exit()

y_arr = np.zeros([4 * n, 1])

for m in range(n):
    y_arr[m, 0] = yi[m]
    y_arr[m + n] = yi[m + 1]

sols = ge(mat, y_arr)

x_vals = np.empty(0)
y_vals = np.empty(0)

for i in range(n):
    ind = i * 4
    abcd_vals = np.empty(0)
    while ind < (i * 4) + 4:
        abcd_vals = np.append(abcd_vals, sols[ind])
        ind += 1
    print(abcd_vals)
    xs = np.linspace(xi[i], xi[i + 1], 100)
    ys = np.empty(0)
    for x in xs:
        ys = np.append(ys, y_value(abcd_vals, xi[i], x))
    x_vals = np.append(x_vals, xs)
    y_vals = np.append(y_vals, ys)

plt.plot(x_vals, y_vals, 'b--')
plt.plot(xi, yi, 'o:')
plt.show()



