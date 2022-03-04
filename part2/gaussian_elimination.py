import numpy as np

matrix = np.array([[3, -2, 1],
                   [-4, -1, 4],
                   [1, -1, 3.0]])
y = np.array([[15],
              [8],
              [13]])
y1 = np.array()

def appender(m, y):
    mprime = np.hstack((m, y))
    return mprime


def pivot(mprime, i):
    n = np.shape(mprime)[0]
    col = mprime[i:n, i]
    j = np.argmax(abs(col)) + i
    return j


print(appender(matrix,y))

print(pivot(matrix, 2))









































'''def appender2(m, y):
    n = np.shape(m)[0]
    newmat = np.empty((n, n + 1))
    for i in range(n):
        for j in range(n):
            newmat[i,j] = m[i,j]
    print(newmat)
'''


