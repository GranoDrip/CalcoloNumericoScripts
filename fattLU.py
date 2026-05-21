"""Fattorizzazione LU di una matrice"""

import numpy as np
from scipy import linalg

A = np.array([[2,1,0,-1],
              [-2,-2,1,-1],
              [4,2,-1,-1],
              [0,2,-3,2]], dtype=float)

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

         