"""Algoritmo di eliminazione di Gauss con tecnica del massimo pivot parziale"""

import numpy as np
import indietro

A = np.array([
    [2, -1, 0, 1], 
    [1, 2, -1, 1], 
    [0, 1, 2, -1], 
    [1, 0, 1, 2]
], dtype=float)

b = np.array([2, 3, 2, 4], dtype=float)

def gauss(a: np.ndarray, b: np.ndarray):

    n = len(a)

    for i in range(n - 1):

        # Massimo pivot parziale
        # i + per riallineare gli indici
        # i + INDICE del numero con VA più grande 
        pivot_row = i + np.argmax(np.abs(a[i:, i]))  

        # Scambio righe su A e b
        a[[i, pivot_row]] = a[[pivot_row, i]] 
        b[[i, pivot_row]] = b[[pivot_row, i]] 

        for j in range(i + 1, n):

            m = a[j, i] / a[i, i] # Coeff per annullare il valore sotto il Pivot

            a[j, i:] = a[j, i:] - m * a[i, i:] # Aggiorno la riga eliminando il componente sotto il pivot
            b[j] = b[j] - m * b[i] # Calcolo i nuovi b

    return a, b

# a,b = gauss(A,b)
# 
# sol = indietro.sostituzione_indietro(a,b)
# 
# print(sol)
