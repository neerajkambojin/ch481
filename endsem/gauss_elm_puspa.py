#Program written after discussion with classmates
import numpy as np

def Guass_Elimination(mat,Y):
#Calling function to append matrix
    M_prime = Append(mat, Y)
    #print(M_prime)
    n = len(mat[0])
#Doing pivoting and elimination in same loop
    for i in range(n):
        M_prime=Pivoting(M_prime,i)
        M_prime = Elimination(M_prime, i)
    #print(M_prime)
#Calling function to solve unknown variables
    x=Back_Substitution(M_prime)
    return x

#To concatenate equation and solution matrix i.e mat and Y
def Append(mat,Y):
    n = len(mat[0])
    M_prime = np.zeros((n, n + 1))
    for i in range(n):
        for j in range(n):
            M_prime[i,j]=mat[i,j]
    for i in range(n):
         M_prime[i,n]=Y[i]
    return M_prime

#For pivoting of appended matrix
def Pivoting(M_prime,i):
    n=len(M_prime)
    col=M_prime[i:n,i]
    j=np.argmax(abs(col))+i
    M_prime[[i, j], :] = M_prime[[j, i], :]
    return M_prime

#For making lower triangle value 0
def Elimination(M_prime,i):
    n = len(M_prime)
    for j in range(i + 1, n):
        M_prime[j,:]-=(M_prime[j,i]/M_prime[i,i])*M_prime[i,:]
    return M_prime

#For calculating value of unknown variables
def Back_Substitution(M_prime):
    n = len(M_prime)
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i+1,n):
            sum += M_prime[i,j]*x[j]
        x[i] =(M_prime[i,n]-sum)/M_prime[i,i]
    return x
