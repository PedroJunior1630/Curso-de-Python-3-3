from time import sleep
def linha():
    print("_-_" * 20)
def maior(* num):
    linha()
    print(f'Analisando os valores...{num}')
    sleep(0.5)
    print(f'Foram informados {len(num)} valores no total.')
    print(f'O maior valor é: {max(num)}')
    linha()
maior(5,6,99,100,132,1,0)
maior(0,0,-1,3,-4,12)
maior(-1,-2,0,-12)
