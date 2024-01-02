from time import sleep
def linha():
    print("-+-" * 20)
def contador(i,f,p):
    if p == 0:
        p = 1
    linha()
    print(f'CONTAGEM DE {i} ATÉ {f} PULANDO DE {abs(p)} EM {abs(p)}')
    linha()
    if i < f:
        f += 1
    else:
        f -= 1
        p = p - (p * 2)
    for c in range(i,f,p):
        print(c,end = " > ")
    print("FIM")

contador(1,10,1)
contador(10,0,2)
linha()
print('Personalize sua contagem!')
print(int(-1))
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo =  int(input('Passo: '))

contador(inicio,fim,passo)
