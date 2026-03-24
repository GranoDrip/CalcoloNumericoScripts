# Esercizio CONGETTURA DI COLLATZ
"""
Sia x0 in input
per n = 1,2,3,4 ... 
Xn+1 = xn/2 se xn è pari
ALTRIMENTI 3xn+1 se è dispari
DETERMINARE:

- Vettore con i valori da x0 a xn
- il piu piccolo intero n tc xn = 1

IN BREVE RITORNARE:
- Sequenza generata
- Numero di iterazioni
"""

def collatz(x0):

    sequenza = []
    n = 0

    while x0 != 1:

        sequenza.append(x0)

        if (x0 % 2 == 0): # SE PARI
            x0 = x0 // 2
        else:
            x0 = (3*x0)+1
        
        n += 1

    sequenza.append(1)  # aggiungo l'ultimo valore

    return sequenza,n


print(collatz(7))