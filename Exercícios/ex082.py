valores = []
valores_par = []
valores_impar = []

while True: 
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    opc = str(input('Deseja continuar?[S/N] ')).upper()
    if opc == "N":
        break
for valor in valores:
    if valor % 2 == 0:
        valores_par.append(valor)
    else:
        valores_impar.append(valor)
print(f'Lista com valores: {valores}')
print(f'Lista com valores par: {valores_par}')
print(f'Lista com valores impares: {valores_impar}')
