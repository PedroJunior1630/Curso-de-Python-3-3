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

def resumo(n,aum,dim):
    print("=+=" *10)
    print(f"RESUMO DO VALOR")
    print("=+=" * 10)
    print(f"Preço analisado: {moeda(n):^20}")
    print(f"Dobro do preço: {dobro(n,True):^20}")
    print(f"Metade do preço: {metade(n,True):^20}")
    print(f"{aum}% de aumento: {aumento(n,aum,True):^20}")
    print(f"{dim}% de redução: {diminui(n,dim,True):^20}")
    print("=+=" * 10)
