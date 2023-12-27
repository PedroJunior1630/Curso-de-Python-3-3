import copy
lista = []
dic = {}
cont = soma = 0
while True:
    cont += 1
    print("=+=" * 20)
    print(f"CADASTRO N° {cont}")
    print("=+=" * 20)
    dic["nome"] = str(input('Nome: ')).strip().title()
    dic["idade"] = int(input('Idade: '))
    dic["sexo"] = str(input('Sexo[F/M]: ')).upper().strip()
    while dic["sexo"] != "M" and dic["sexo"] != "F":
        print("ERRO! Os valores aceitos são apenas F e M")
        dic["sexo"] = str(input('Sexo[F/M]: ')).upper().strip()
    lista.append(copy.deepcopy(dic))
    print("=+=" * 10)
    opc = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    while opc != "S" and opc != "N":
        print("ERRO! Os valores aceitos sao apenas S ou N")
        opc = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if opc == "N":
        break

print("=+=" * 20)
print(f"(A)Tivemos {cont} pessoas cadastradas.")

for contador,nada in enumerate(lista):
    for chave,valor in lista[contador].items():
        if chave == "idade":
            soma += valor
media = soma / cont
print(f"(B) A média de idade deste grupo é de {media:.1f} anos.")


print("(C) As mulheres do grupo são: ",end = "")
for contador,nada in enumerate(lista):
    for chave,valor in lista[contador].items():
        if chave == "sexo" and valor == "F":
            for c,v in lista[contador].items():
                if c == "nome":
                    print(f'{v};',end = " ")

print('\n(D) Lista de pessoas acima da média: ')
for contador,nada in enumerate(lista):
    for chave, valor in lista[contador].items():
        if chave == "idade" and valor > media:
            for c,v in lista[contador].items():
                print(f'{c} = {v};',end = " ")
            print()