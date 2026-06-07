"""Fattorizzazione LU di una matrice"""

import numpy as np


A = np.array([[-1 , 1 ,-3 , 1 , 1 ],
              [ 1 ,-2 , 0 , 0 , -1],
              [ 0 ,-2 , 2 , 3 , -2 ],
              [ 0 , 0 , 1 ,-2 , 0],
              [ 0 , 0 , 0 , 2 , 0]], dtype=float)

def fatt_LU(a:np.ndarray):

    L = np.eye(a.shape[0])
    U = a.copy()

    n = a.shape[0] # Dimensione della matrice

    for i in range(n-1):
        pivot = U[i][i]

        for j in range (i+1,n):
            mul = U[j,i] / pivot
            L[j,i] = mul
            
            U[j, :] = U[j, :] - mul * U[i, :]

    return L,U

l,u = fatt_LU(A)

print(l)
print("\n")
print(u)


         