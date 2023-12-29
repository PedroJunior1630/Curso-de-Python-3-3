dic = {}
gols = []
lista = []
cod = 0
while True:
    cod += 1
    dic["cod"] =  cod
    dic["jogador"] = str(input('Nome do jogador: ')).strip().title()
    dic["partidas"] = int(input('Partidas: '))
    for c in range(0,dic["partidas"]):
        gols.append(int(input(f'{c+1}° Partida gols marcados:')))
    dic["gols"] = gols[:]
    dic["total"] = sum(gols)
    lista.append(dic.copy())
    dic.clear()
    gols.clear()
    opc = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if "N" in opc:
        break
print("=+=" * 30)
print(f"{'COD':^15} {'NOME':^15} {'PARTIDAS':^15} {'GOLS':^15} {'TOTAL':^15}")
for sta in lista:
    for valor in sta.values():
        print(f"{str(valor):^15}",end= " ")
    print()
print("=+=" * 30)
while True:
    while True:
        dados = int(input('Deseja mostrar dados de qual jogador?(999 para parar): '))
        if dados == 999:
            break
        elif dados > len(lista) or dados-1 < 0:
            print("-+-" * 20)
            print(f"ERRO! O jogador {dados} não existe!")
        elif dados >= 1 and dados <= len(lista):
            break
    if dados == 999:
        break
    print("=+=" * 20)
    print(f"Levantamento do jogador {lista[dados-1]['jogador']}")
    for cont,gols in enumerate(lista[dados-1]["gols"]):
        print(f'No jogo {cont} fez {gols} gol(s).')
    print("=+=" * 20)
