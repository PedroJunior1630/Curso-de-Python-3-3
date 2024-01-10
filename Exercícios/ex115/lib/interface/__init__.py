def leiaInt(msg):
    while True:
        try:
            num = int(input(f"\033[1;97m{msg}"))
        except KeyboardInterrupt:
            print("\033[1;31m O usuario preferiu não digitar o número.")
        except:
            print(f'\033[1;31mERRO! Por favor digite um número inteiro válido.')
        else:
            return num


def linha(tam=15):
    print("=+=" * tam)


def cabecalho(texto):
    linha()
    print(texto.center(45))
    linha()


def menu(opc):
    cabecalho("MENU PRINCIPAL")
    for contador, item in enumerate(opc):
        print(f'\033[36m{contador+1}-\033[m \033[97m{item}\033[m')

