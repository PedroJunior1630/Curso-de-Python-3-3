dicionario = {}
nome = str(input('Digite o nome: '))
media = float(input(f'Média de {nome}: '))
dicionario["nome"] = nome
dicionario["media"] = media
if media < 6:
    dicionario["situação"] = "Reprovado"
else:
    dicionario["situação"] = "Aprovado"
for chave, valor in dicionario.items():
    print(f'{chave.capitalize()} é igual a {valor}')
