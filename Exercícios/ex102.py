import math
def fatorial(num, mostrar = False):
    """
    fatorial -> Metódo para calcular fatorial
    num -> Número da fatorial que deseja ser calculado
    mostrar -> True para mostrar a formúla e False apenas para o resultado.
    return -> retorna o resultado
    """
    fact = 1
    if mostrar == True:
        for c in range(num,0,-1):
            print(f'{c}',end = " ")
            fact *= c
            if c == 1:
                print("=",end=" ")
            else:
                print("x",end=" ")
        return fact
    else:
        return math.factorial(num)
print(fatorial(5,True))
help(fatorial)
