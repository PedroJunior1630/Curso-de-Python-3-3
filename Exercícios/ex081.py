lista = []
cont = 0
while True:
    valor = int(input('Digite um valor: '))
    cont += 1
    lista.append(valor)
    opc = str(input("Deseja continuar?[S/N]")).upper()
    if opc == "N":
        break
lista.sort(reverse=True)
print(f'Foram digitados {cont} elementos.')
print(f'A lista em ordem decrescente: {lista}')
if 5 in lista:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")
    