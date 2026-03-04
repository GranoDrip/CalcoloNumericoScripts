# Implementazione METODO DELLE SUCCESSIVE BISEZIONI
import math

def f(x:int):
    """
    Qualsiasi funzione che abbia uno zero
    """
    return 3*(math.exp(x-(3/2)))-3 

def bisezioni(f,a,b,tol,itmax):
    """
    f: Funzione in cui ricercare uno zero \\
    a,b: Estremi dell'intervallo \\
    tol: tolleranza richiesta \\
    itmax: massimo numero di iterazioni consentite 

    RITORNA:
    c: approssimazione di uno zero \\
    it: iterazioni effettuate 
    """

    # Verifico che soddisfi la condizione del T. degli zeri
    if (f(a)*f(b) >= 0):
        print("NON SODDIFA IL T. DEGLI ZERI")
        return
    
    # Cerco l'approssimazione 
    it = 0 # Iterazioni
    arresto = 0 # Variabile booleana ==> Se è diversa da 0 devo fermare l'iterazione
    while it < itmax and not arresto:
        it += 1
        c = (a+b)/2
        if (f(c) == 0):
            print(f"Trovato lo zero in: {c} ")
            return it,c 
        elif (f(a)*f(c) < 0):
            b = c
        else:
            a = c
        arresto = (b-a) < tol

#    if (not arresto):
#        print("Convergenza non raggiunta :(")

    print(f"Approssimazione: {c}")
    print(f"Iterazioni: {it}")
    
    return it,c

bisezioni(f,0,5,1e-10,100)