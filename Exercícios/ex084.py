pessoas = list()
cadastro = list()
maiorpeso = list()
menorpeso = list()
maior = menor = cont = 0
while True:
    cadastro.append(input('Nome: '))
    cadastro.append(float(input('Peso: ')))
    pessoas.append(cadastro[:])
    cadastro.clear()
    opc = str(input('Deseja continuar?[S/N] ')).upper()
    if "N" in opc: 
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
for peso in pessoas:
    cont += 1
    if cont == 1:
        maior = peso[1]
        menor = peso[1]
        maiorpeso.append(peso[0])
        menorpeso.append(peso[0])
    else:
        if peso[1] >= maior:
            if peso[1] == maior:
                maiorpeso.append(peso[0])
            if peso[1] > maior:
                maior = peso[1]
                maiorpeso.clear()
                maiorpeso.append(peso[0])
        if peso[1] <= menor:
            if peso[1] == menor:
                menorpeso.append(peso[0])
            if peso[1] < menor:
                menor = peso[1]
                menorpeso.clear()
                menorpeso.append(peso[0])
print(f'Peso máximo registrado: {maior}Kg das pessoas: {maiorpeso}')
print(f'Peso mínimo registrado: {menor}Kg das pessoas: {menorpeso}')
