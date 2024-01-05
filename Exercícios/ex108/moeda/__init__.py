def metade(n):
    return n / 2

def dobro(n):
    return n * 2

def aumento(n, por= 0):
    aum = n + (n * por / 100)
    return aum

def diminui(n, por =0):
    dim = n - (n * por / 100)
    return dim

def moeda(n):
    mostra = (f"R${n:.2f}")
    return(str(mostra).replace('.',','))
