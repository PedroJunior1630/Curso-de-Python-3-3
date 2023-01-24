#Passo 1 ler 5 valores e guardar em uma lista
valores = [int(input('Digite o valor para a posição 0: ')),
           int(input('Digite o valor para a posição 1: ')),
           int(input('Digite o valor para a posição 2: ')),
           int(input('Digite o valor para a posição 3: ')),
           int(input('Digite o valor para a posição 4: '))]
ma = max(valores)
mi = min(valores)
print(f'Você digitou os valores: {valores}')
print(f'Maior valor: {ma} nas posições: ',end = "")
for pos,valor in enumerate(valores):
    if valor == ma:
        print(f'\033[1;36m{pos}...',end = " ")

print(f'\nMenor valor: {mi} nas posições: ',end = "")
for pos,valor in enumerate(valores):
    if valor == mi:
        print(f'\033[1;33m{pos}...',end = " ")

#Passo 3 mostrar as respectivas posições dos números
