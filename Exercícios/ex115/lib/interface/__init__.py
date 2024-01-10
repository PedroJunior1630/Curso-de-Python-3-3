def linha(tam=15):
    print("=+=" * tam)

def cabecalho(texto):
    linha()
    print(texto.center(90))
    linha()

def menu(opc):
    for contador, item in enumerate(opc):
        print(f'\033[36m{contador+1}-\033[m \033[97m{item}\033[m')
