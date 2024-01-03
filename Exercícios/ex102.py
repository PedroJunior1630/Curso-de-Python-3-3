import math
def fatorial(num, mostrar = False):
    """
    fatorial -> Metódo para calcular fatorial
    num -> Número da fatorial que deseja ser calculado
    mostrar -> True para mostrar a formúla e False apenas para o resultado.
    return -> retorna o resultado
    """
    fact = 1

    print("=+=" * 10)
    for c in range(num,0,-1):
        if mostrar == True:
            print(f'{c}',end = " ")
            if c == 1:
                print("=",end=" ")
            else:
                print("x",end=" ")
        fact *= c
    return fact

print(fatorial(5,True))
help(fatorial)
