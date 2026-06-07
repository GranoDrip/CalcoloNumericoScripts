import numpy as np
import matplotlib.pyplot as plt

# ES 3 interpolazione
def f(x):
    return pow(np.e,-x) * np.sin(x*2)

def g(x): # Funzione di runge
    return 1 / (1+pow(x,2))


# ES 1 INTERPOLAZIONE
def polinomio_interpolante(x, y, xx):
    x = np.array(x)
    y = np.array(y)
    xx = np.array(xx)
    
    n = len(x)
    yy = np.zeros(len(xx))
    
    for i in range(len(xx)):
        p = xx[i]
        valoreInterpolato = 0
        
        for j in range(n):
            # Calcolo del polinomio di base di Lagrange L_j
            L_j = 1
            for k in range(n):
                if k != j:
                    L_j *= (p - x[k]) / (x[j] - x[k])
            
            valoreInterpolato += y[j] * L_j
            
        yy[i] = valoreInterpolato
        
    return yy

# 2 Grafico interpolazione
def grafico_interpolazione(f, a, b, n):
    x = np.linspace(a, b, n)
    y = f(x)
    
    # Generazione di ascisse fitte per tracciare le curve
    xx = np.linspace(a, b, 500)
    
    # Valutazione della funzione esatta e del polinomio interpolante
    yy_f = f(xx)
    yy_p = polinomio_interpolante(x, y, xx)
    
    # Creazione del grafico con i tre elementi richiesti
    plt.figure(figsize=(8, 6))
    plt.plot(xx, yy_f, label="Funzione esatta f(x)", color="blue")
    plt.plot(xx, yy_p, label="Polinomio interpolante", color="red", linestyle="--")
    plt.scatter(x, y, color="black", zorder=5, label="Nodi di interpolazione")
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

grafico_interpolazione(f,0,np.pi,10)