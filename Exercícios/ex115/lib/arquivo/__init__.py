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
