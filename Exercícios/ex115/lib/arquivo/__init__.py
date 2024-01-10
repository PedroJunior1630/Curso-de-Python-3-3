from ex115.lib.interface import * 
def arquivoExiste(arq):
    try:
        var = open(arq,"rt")
    except:
        return False
    else:
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
        for linha in var:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n","")
            print(f"{dado[0]:.<30}{dado[1]:>3} anos")
    finally:
        var.close()

def cadastrarPessoa(arq, n, i):
    try:
        var = open(arq, "at")
    except:
        print("Houve um ERRO na abertura do arquivo.")
    else:
        try:
            var.write(f"{n};{i}\n")
        except:
            print("Houve um ERRO no ao registrar os dados.")
        else:
            print(f"Novo registro de {n} adicionado.")
