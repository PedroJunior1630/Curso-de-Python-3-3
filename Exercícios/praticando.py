"""import os
def limpaTela():
    os.system('cls')

"""limpaTela()
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
RED = '\033[1;91m'
RESET = '\033[0m'

while True:
    num = int(input('\033[1;32mDigite um número de 0 até 20: '+ RESET))
    if num < 0 or num > 20:
        print(RED +'OPÇÃO ERRADA! TENTE NOVAMENTE'+RESET)
        limpaTela()
    else:
        print(f'\033[1;36mO número {num} escrito por extenso é: {numeros[num]}'+ RESET)
        op = str(input('\033[1;33mDeseja continuar? [S/N]: '+ RESET)).upper().strip()
        limpaTela()
        if op == 'N':
            break
        else:
            continue"""
