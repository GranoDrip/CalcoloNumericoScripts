"""Algoritmo di sostituzione in avanti per la risoluzione di ST Inferiori"""
import numpy

L = numpy.array([
    [2,0,0],
    [1,3,0],
    [4,2,1]
],dtype=float) # Matrice triangolare inferiore ( Lower )
b = numpy.array([2,5,6],dtype=float) # Termini noti

def sostituzione_avanti(L:numpy.matrix,b:list):

    n = len(b) # Lunghezza dei termini noti
    x = numpy.zeros(n)

    for i in range(n):
        sum = b[i]

        for j in range(i):
            sum -= L[i][j] * x[j]

        x[i] = sum / L[i][i]

    return x
        

x = sostituzione_avanti(L,b)

for v in x:
    print(v)