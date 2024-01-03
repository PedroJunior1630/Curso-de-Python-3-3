dicionario = {}

def notas(*notas,sit=False):
    """
    -> Função para analisar a média de uma turma pela leitura de várias notas
    notas: uma ou mais notas armazenadas
    sit: situação a ser mostrada caso seja True, False é valor padrão.
    return: retorna um dicionário com várias informações
    """
    print("+=+" * 20)
    dicionario["Quantidade"] = len(notas) 
    dicionario["Maior nota"] = max(notas)
    dicionario["Menor nota"] = min(notas)
    dicionario["Média da turma"] = sum(notas) / len(notas)
    if sit == True:
        if dicionario["Média da turma"] <= 5:
            dicionario["Situação"] = "RUIM"
        elif 5 < dicionario["Média da turma"] <= 7:
            dicionario["Situação"] = "RAZOAVÉL"
        else:
            dicionario["Situação"] = "BOA"
    return dicionario


resp = notas(9.7,7.6,5.4,6,5.4,5,sit=True)
print(resp)
