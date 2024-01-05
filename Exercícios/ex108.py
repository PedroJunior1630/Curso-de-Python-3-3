from ex108 import moeda

p = float(input("Digite o preço: R$"))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 15% é {moeda.moeda(moeda.aumento(p,15))}')
print(f'Reduzindo 17% é {moeda.moeda(moeda.diminui(p,17))} ')
