# Metodo di newton
"""
Sia x0 una stima si procede con:
xn = xn-1 - f(xn-1)/ f'(x-n1)
"""

def f(x, der=0):
    if der == 0:
        return x**2 - 2 # f
    else:
        return 2*x #f'
    
def newton(f,x0,tol,itmax,debug=False):
    it = 0 # Iterazioni
    arresto = 0

    while arresto != True and it < itmax:
        it += 1
        x1 = x0 - (f(x0)/f(x0,1))
        arresto = abs(x1-x0) < tol
        x0 = x1
        if debug: # Serve a vedere la convergenza
            print(x0)
        
    if not arresto:
        print("Convergenza non raggiunta")
        
    print("Alpha: " + str(x1))
    print("Iterate: " + str(it))


newton(f,1.4,1e-13,200)