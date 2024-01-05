from ex109 import moeda

p = float(input("Digite o preço: R$"))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando 15% é {moeda.aumento(p,15,True)}')
print(f'Reduzindo 17% é {moeda.diminui(p,17,True)} ')
