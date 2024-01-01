print("-+-" * 20)
print("CALCULANDO ÁREA")
print("-+-" * 20)

def calculaArea(l,c):
    area = l * c
    print(f'As dimensões de {l:.2f}x{c:.2f}m² tem uma área de {area:.2f}m²')

larg = float(input('Largura(m): '))
comp = float(input('Comprimento(m): '))

calculaArea(larg,comp)
