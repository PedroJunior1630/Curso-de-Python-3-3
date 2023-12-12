matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = soma3 = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l] [c] = int(input(f'Digite um elemento na posição [{l},{c}] '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end = " ")
    print()

print(f'A soma de todos os valores pares: {soma}')
print(f'A soma dos valores da terceira coluna: {soma3}')
print(f'O maior valor da segunda linha: {maior}')
