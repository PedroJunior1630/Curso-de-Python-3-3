import random

numeros = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))

print(f'\033[1;32mNúmeros sorteados: {numeros}')
print(f'Maior valor: {max(numeros)}')
print(f'Menor valor: {min(numeros)}')
