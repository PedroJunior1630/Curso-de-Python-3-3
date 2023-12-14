import random
megasena = [0, 0, 0, 0, 0, 0]

palpites = int(input('Quantos palpites você deseja: '))
print("=+=" * 20)
for p in range(0,palpites):
    for j in range(0,6):
        megasena[j] = random.randint(1,60)
        if megasena[j] == megasena[j-1]:
            megasena[j] = random.randint(megasena[j+1],60)
    megasena.sort()
    print(f'{p+1}° JOGO : {megasena}')
print("=+=" * 20)
