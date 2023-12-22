dicionario = {}
dicionario["nome"] = str(input('Digite o nome: ')).capitalize().strip()
dicionario["nascimento"] = int(input('Ano de nascimento: '))
dicionario["ctps"] = int(input('Tem carteira de trabalho?(0 para não): '))
ano_atual = 2023
dicionario["idade"] = ano_atual - dicionario["nascimento"]
if dicionario["ctps"] != 0:
    dicionario["contratação"] = int(input('Digite o ano de contratação: '))
    dicionario["salário"] = float(input('Digite o salário: R$ '))
    dicionario["aposentadoria"] = (30 - (2023 - dicionario["contratação"])) + dicionario["idade"]
print(dicionario)
for chave, valor in dicionario.items():
    print(f'{chave} tem o valor {valor}')
