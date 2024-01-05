from ex107 import moeda

p = float(input("Digite o preço: R$"))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 15% é {moeda.aumento(p,15)}')
print(f'Reduzindo 17% é {moeda.diminui(p,17)} ')
