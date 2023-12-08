parenteses_aberto = []
parenteses_fechado = []
equa = str(input('Digite a equação: '))
for x in equa:
    if x == '(':
        parenteses_aberto.append(x)
    elif x == ')':
        parenteses_fechado.append(x)

if len(parenteses_aberto) == len(parenteses_fechado):
    print('Equação correta.')
else:
    print('Equação incorreta!')
