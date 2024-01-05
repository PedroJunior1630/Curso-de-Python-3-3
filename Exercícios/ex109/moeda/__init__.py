def metade(n, mostrar=False):
    if mostrar == True:
        return(moeda(n/2))
    else:
        return n / 2

def dobro(n, mostrar=False):
    if mostrar == True:
        return(moeda(n*2))
    else:
        return n * 2

def aumento(n, por= 0,mostrar=False):
    aum = n + (n * por / 100)
    if mostrar == True:
        return(moeda(aum))
    else:
     return aum

def diminui(n, por =0,mostrar=False):
    dim = n - (n * por / 100)
    if mostrar == True:
        return(moeda(dim))
    else:
        return dim

def moeda(n):
    mostrar = (f"R${n:.2f}")
    return(str(mostrar).replace('.',','))