"""Calcola il rango della matrice ridotta ( Algoritmo di Gauss )"""

from gauss import gauss
import numpy as np

A = np.array([
    [1, 2, -1, 3],
    [2, 4, 1, 0],
    [-1, 1, 2, 1],
    [3, 6, 0, 3]
], dtype=float)

b = np.array([5, 7, 2, 12], dtype=float)

def rank(matrix: np.ndarray):
    rank = 0 # Rango della matrice
    row,col = matrix.shape # Estraggo le righe e le colonne

    for i in range(row): # Per ogni riga
        valida = False # Assumo che la riga su cui lavoro è nulla

        for j in range(col): # per ogni elemento della riga
            if(round(matrix[i,j],10) != 0): # Arrotondo il valore
                valida = True
                break

        if valida:
            rank += 1

    return rank


a,b = gauss(A,b) # Prima riduco a gradini
r = rank(a) # Dopo calcolo il rank

print("Rank : " + str(r))