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
    soma  += dic["idade"]
    dic["sexo"] = str(input('Sexo[F/M]: ')).upper().strip()
    while dic["sexo"] != "M" and dic["sexo"] != "F":
        print("ERRO! Os valores aceitos são apenas F e M")
        dic["sexo"] = str(input('Sexo[F/M]: ')).upper().strip()
    lista.append(dic.copy())
    print("=+=" * 10)
    opc = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    while opc != "S" and opc != "N":
        print("ERRO! Os valores aceitos sao apenas S ou N")
        opc = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if opc == "N":
        break

print("=+=" * 20)
print(f"(A) Tivemos {len(lista)} pessoas cadastradas.")

media = soma / len(lista)
print(f"(B) A média de idade deste grupo é de {media:.1f} anos.")

print("(C) As mulheres do grupo são: ",end = "")
for mulheres in lista:
    if mulheres["sexo"] == "F":
        print(f'{mulheres["nome"]};',end = " ")

print('\n(D) Lista de pessoas acima da média: ')
for pessoas in lista:
    if pessoas["idade"] > media:
        for chave, valor in pessoas.items():
            print(f'{chave} = {valor};',end = " ")
        print()
