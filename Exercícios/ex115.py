from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arquivo = "cadastro.txt"
if arquivoExiste(arquivo) == False:
    arquivoCriar(arquivo)
while True:
    menu(["Visualizar a lista de Pessoas","Cadastrar Pessoas","Sair do Programa"])
    opcao = leiaInt("\033[32mQual opção deseja?\033[m")
    if opcao == 1:
        cabecalho("PESSOAS CADASTRADAS")
        exibirArquivo(arquivo)
    elif opcao == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: ")).strip().title()
        idade = leiaInt("Idade: ")
        cadastrarPessoa(arquivo,nome,idade)
    elif opcao == 3:
        cabecalho("Sistema finalizando... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!")
    sleep(2)
    