from random import randint
numeros = []

def sorteia(num):
    for c in range(5):
        num.append(randint(0,10))
    print(f'Os números sorteados foram: {num}')

def somaPar(num):
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos números pares em {num} é igual a {soma}')

sorteia(numeros)
somaPar(numeros)
