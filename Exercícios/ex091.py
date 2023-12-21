from random import randint
dicionario = {}
print("=+=" * 20)
for jogada in range(1,5):
    dicionario[f"jogador{jogada}"] = randint(1,6)
for chave, valor in dicionario.items():
    print(f'{chave.capitalize()} tirou {valor}')
print("=+=" * 20)
print(f"{'RAKING':>20}")
print('=+=' * 20)
c = 1
for valor in sorted(dicionario, key = dicionario.get, reverse = True):
    print(f"{c}° lugar {valor} com {dicionario[valor]}")
    c += 1
