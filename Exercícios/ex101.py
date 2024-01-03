def linha():
    print("=+=" * 10)


def vota(nasc):
    from datetime import date
    ano =  date.today().year
    idade = ano - nasc
    linha()
    print(f'Com {idade} anos de idade: ',end = "")
    if idade < 18:
        return "NÃO VOTA"
    elif idade >= 18 and idade <= 65:
        return "VOTO OBRIGATÓRIO"
    elif idade > 65:
        return "VOTO OPCIONAL"


linha()
print("VOTAÇÃO")
linha()
nascimento = int(input('Ano de nascimento: '))
print(vota(nascimento))
linha()