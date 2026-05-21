"""
Formula per l'approssimazione del PI di leibniz
4*(1/1-1/3+1/5- ...)

INPUT:
    - tol: VALORE DA NON SUPERARE
    - itmax: NUMERO MASSIMO DI ITERATE
OUTPUT:
    - pi Approssimato
"""

def leibnizApprox(tol,itmax):

    it = 0
    sum = 0
    segno = 1
    den = 1

    while it < itmax:
        termine = segno * (1 / den)
        sum += termine

        if abs(termine) < tol:
            return 4*sum

        den += 2
        segno *= -1
        it +=1

    print("Iterate raggiunte")
    return 4*sum

print(leibnizApprox(1e-4,6000))