"""Calcola la matrice inversa usando la fattorizzazione LU ( A = LU )

   Per ogni colonna ei dell'identita I si ricava la colonna dell'inversa
   in quanto AX = I
   
"""
import numpy as np
from fattLU import fatt_LU
from inavanti import sostituzione_avanti
from indietro import sostituzione_indietro

A = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
], dtype=float)

def inversa(a:np.ndarray):
    l,u = fatt_LU(a) # Creo le matrici L ed U per A
    n = len(a) # dimensione di A

    idty = np.eye(n) # Matrice identità
    sol = np.zeros(shape=(n,n)) # Matrice di zeri ( vuota )

    for i in range(n):
        e = idty[:,i] # Colonna ei

        # Risolvo i sistemi lineari
        y = sostituzione_avanti(l,e)
        x = sostituzione_indietro(u,y)

        sol[:,i] = x
    
    return sol


# print("Matrice Inversa calcolata:")
# print(np.round(inversa(A),10))
# 
# print("\nVerifica A * A^-1 (dovrebbe essere l'Identità):")
# identita_calcolata = np.dot(A, inversa(A))
# print(np.round(identita_calcolata, 10))

