tabela = ('Gabinete',225,'Placa mãe',175,'I7 7700K',380,'GTX 1050Ti',1250,'SSD 512GB',350,'Memória RAM 8GB DDR4 2666mhz',315)
print('=+=' * 20)
print(f'{"LISTAGEM DE PREÇOS ELETRONICAS":^60}')
print('=+=' * 20)
for posicao in range(0,len(tabela)):
    if posicao % 2 == 0:
        print(f'{tabela[posicao]:.<30}',end = "")
    else:
        print(f'R$ {tabela[posicao]:.2f}')
