"""Algoritmo di sostituzione all'indietro per la risoluzione di ST Superiori"""
import numpy

U = numpy.array([
    [1,0,0],
    [0,1,0],
    [0,0,1]
],dtype=float) # Matrice triangolare inferiore ( Upper )
b = numpy.array([1,2,3],dtype=float) # Termini noti

def sostituzione_indietro(u:numpy.array,b:list):
    n = len(b)
    x = numpy.zeros(n)
    x[n-1] = b[n-1] / u[n-1][n-1]


    for i in range(n-2,-1,-1):
        sum = b[i]

        for j in range (i+1,n):
            sum -= u[i][j] * x[j]
        
        x[i] = (1/u[i][i]) * sum

    return x

x = sostituzione_indietro(U,b)

for v in x:
    print(v)


