nums =  ('Zero','Um','Dois','Três', 'Quatro', 'Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    num = int(input('\033[1;30mDigite um número de 0 a 20: '))
    
    if num < 0 or num > 20:
        print('TENTE NOVAMENTE.',end = '')
    else:
        print(f'\033[1;32mO número {num} escrito por extenso é {nums[num]}')
        opcao = str(input('Deseja continuar? [S/N] ')).upper()
        
        if opcao[0] == 'N':
            break
