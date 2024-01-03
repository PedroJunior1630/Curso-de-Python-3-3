def ficha(jogador="indefinido",gols="0"):
    print("+=+" *10)
    print(f"O jogador {jogador} marcou {int(gols)} gols.")


print("+=+" * 10)
jog = str(input("Nome do jogador: ")).strip()
gol = str(input("Marcou quantos gols: ")).strip()

if jog == "" and gol == "":
    ficha()
elif jog == "":
    ficha(gols=gol)
elif gol == "":
    ficha(jog)
else:
    ficha(jog,gol)