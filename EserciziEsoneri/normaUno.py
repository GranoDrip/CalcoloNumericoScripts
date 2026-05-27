"""Calcola la norma uno di una matrice
    La norma uno è definita come IL MASSIMO tra 1 e n della somma del valore assoluto degli elementi in colonna delle matrici
"""

import numpy as np

A = np.array([[1,2],
             [-3,-2],
             [-1,-3]])

def normaUno(a: np.ndarray):

    colonne = []

    row,col = a.shape

    for i in range(col):
        sum = 0
        for j in range(row):
            sum += abs(a[j, i])
        colonne.append(sum)
    
    return max(colonne)

print(normaUno(A))
        
    
