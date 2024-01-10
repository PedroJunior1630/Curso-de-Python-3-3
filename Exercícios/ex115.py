from ex115.lib.interface import *
from time import sleep
while True:
    menu(["Visualizar a lista de Pessoas","Cadastrar Pessoas","Sair do Programa"])
    opcao = leiaInt("\033[32mQual opção deseja?\033[m")
    if opcao == 1:
        cabecalho("OPÇÃO 1")
    elif opcao == 2:
        cabecalho("OPÇÃO 2")
    elif opcao == 3:
        cabecalho("Sistema finalizando... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!")
    sleep(2)