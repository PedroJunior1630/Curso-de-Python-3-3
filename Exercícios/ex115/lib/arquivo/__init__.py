from ex115.lib.interface import * 
def arquivoExiste(arq):
    try:
        var = open(arq,"rt")
    except:
        print("ERROR")
        return False
    else:
        print("EXISTE")
        return True


def arquivoCriar(arq):
    a = open(arq, "wt+")
    a.close()


def exibirArquivo(arq):
    try:
        var = open(arq,"rt")
    except:
        print("ERRO AO EXIBIR O ARQUIVO")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        print(var.read())

