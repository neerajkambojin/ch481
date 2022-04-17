import numpy as np
import matplotlib.pyplot as plt

xi = np.linspace(100, 300, 21)
yi = [0.429798, 0.352640, 0.289338, 0.237408, 0.194852, 0.160559, 0.164582, 0.273047, 0.483905, 0.724760, 0.908118,
      0.992072, 0.979871, 0.900932, 0.790204, 0.671060, 0.548327, 0.414375, 0.307015, 0.251896, 0.206746]
n = len(yi) - 1

matX = np.zeros([4 * n, 4 * n], float)
for i in range(n):
    matX[i, (4 * i) + 3] = 1

h = xi[1] - xi[0]
k = 0
l = k + 4
for j in range(n, 2 * n):
    dino = 1
    l = k + 4
    while k < l:
        matX[j, k] = (h ** 3) / dino
        dino *= h
        k += 1

tmp = 0
for i in range(2 * n, 3 * n - 1):
    nimo = 3 * (h ** 2)
    div = 1
    for k in range(4 * tmp, 4 * (tmp + 1) - 1):
        matX[i, k] = nimo / div
        if k == 4 * tmp:
            div = 1.5 * h
        else:
            div = 3 * (h ** 2)
    matX[i, k + 4] = -1
    tmp += 1

j = 0
for i in range((3 * n) - 1, (4 * n) - 2):
    matX[i, j] = 3 * h
    matX[i, j + 1] = 1
    matX[i, j + 5] = -1
    j += 4

matX[((4 * n) - 2), 0] = 6 * h
matX[((4 * n) - 2), 1] = 2
matX[((4 * n) - 1), ((4 * n) - 4)] = 6 * h
matX[((4 * n) - 1), ((4 * n) - 3)] = 2

matY = np.zeros(4 * n)
for m in range(n):
    matY[m] = yi[m]
    matY[n + m] = yi[m + 1]


def combine_mats(M, Y):
    n = len(M[0])
    MP = np.zeros((n, n + 1))
    MP[:, 0:n] = M
    MP[:, n] = Y
    return MP


## Pivoting MP along column i
def pivot(MP, i):
    n = len(MP)
    X = MP[i:n, i]
    j = np.argmax(abs(X)) + i
    MP[[i, j], :] = MP[[j, i], :]
    return MP


## Elimination of MP along column i
def eliminate(MP, i):
    N = np.shape(MP)[0]
    for j in range(i + 1, N):
        fac = MP[j, i] / MP[i, i]
        MP[j, :] -= MP[i, :] * fac
    return MP


## Solving for tri-diagonal matrix
def solve_tri_diagonal(MP):
    N = np.shape(MP)[0]
    X = np.zeros(N)
    mat = MP[:, 0:N]
    Y = MP[:, N]
    for i in range(N - 1, -1, -1):
        fac = 0.0
        for j in range(i + 1, N):
            fac += mat[i, j] * X[j]
        X[i] = (Y[i] - fac) / mat[i, i]
    return X


## For input mat,Y, returns X s.t. mat.X=Y
def GaussElimination(mat, Y):
    N = np.shape(mat)[0]
    # X = np.zeros(N)
    MP = combine_mats(mat, Y)
    for i in range(N):
        MP = pivot(MP, i)
        MP = eliminate(MP, i)

    X = solve_tri_diagonal(MP)
    return X


sols = GaussElimination(matX, matY)

a_values = np.empty([n])
b_values = np.empty([n])
c_values = np.empty([n])
d_values = np.empty([n])

j = 0
k = 0
for i in range(n):
    a_values[j] = sols[k]
    b_values[j] = sols[k + 1]
    c_values[j] = sols[k + 2]
    d_values[j] = sols[k + 3]
    k += 4
    j += 1
def y_i(abcd, x_i, x):
    y = 0
    for i in range(4):
        y += (abcd[i] * (pow((x - x_i), (3 - i))))
    return y
x_values = np.empty(0)
y_values = np.empty(0)
for i in range(n):
    abcd = [a_values[i], b_values[i], c_values[i], d_values[i]]
    xs = np.linspace(xi[i], xi[i+1], 50)
    for x in xs:
        x_values = np.append(x_values, x)
        y_value = y_i(abcd, xi[i], x)
        y_values = np.append(y_values, y_value)

plt.plot(x_values, y_values, 'b--')
plt.plot(xi, yi, 'ro:', alpha=0.45)
plt.show()
