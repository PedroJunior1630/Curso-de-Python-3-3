dicionario = {}
lista = []
soma = 0
dicionario["Nome"] = str(input('Digite o nome do jogador: ')).capitalize().strip()
partidas = int(input('Quantas partidas jogou? '))
for i in range(0,partidas):
    lista.append(int(input(f'Marcou quantos gols na partida {i+1}°: ')))
    soma += lista[i]
dicionario["Gols"] = lista
dicionario["Total"] = soma
print("=+=" * 30)
print(dicionario)
print("=+=" * 30)
for chave,valor in dicionario.items():
    print(f'O campo {chave} tem o valor {valor}')
print(f'O jogador {dicionario["Nome"]} jogou {partidas}.')
print("=+=" * 30)
for num,valor in enumerate(lista):
    print(f'{num+1}° Jogo marcou: {valor} gols.')
print(f'Um total de {soma} gols.')
