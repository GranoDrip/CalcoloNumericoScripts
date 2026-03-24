# Esonero del 07-04-2025
# Scrivere una funzione che contenga in un array tutti i numeri di fibonacci compresi tra n,m

# s: inizio
# e: fine

# Approccio iterativo
def fibonacci(s,e):
    
    a = 1
    b = 1

    risultato = [] # Risultato

    while a <= e:

        if (a >= s):
            risultato.append(a)
        
        xn = a + b
        a = b
        b = xn

    return risultato

print(fibonacci(2,13))
