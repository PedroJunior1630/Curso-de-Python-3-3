lista = []

while True:
    valor = int(input('\033[1;33mDigite um valor: '))
    if valor in lista:
        print(f'\033[1;31mValor {valor} já foi adicionado!')
    else:
        lista.append(valor)
    opc = str(input('\033[1;36mDeseja continuar?[S/N]')).upper()
    if opc == "N":
        break
lista.sort()
print(f'\033[1;97mLista em ordem crescente: {lista}')
