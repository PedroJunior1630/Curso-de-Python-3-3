def ficha(jogador="desconhecido",gols="0"):
    print("+=+" *10)
    print(f"O jogador {jogador} marcou {int(gols)} gol(s).")


print("+=+" * 10)
jog = str(input("Nome do jogador: ")).strip()
gol = input("Marcou quantos gols: ")

if jog == "" and gol.isnumeric() == False:
    ficha()
elif jog == "":
    ficha(gols=gol)
elif gol.isnumeric() == False:
    ficha(jog)
else:
    ficha(jog,gol)
