numeros = [[], []]

for n in range(1,8):
    num = int(input(f'Digite o {n}° número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()

print(f"Números pares: {numeros[0]}")
print(f"\nNúmeros impares: {numeros[1]} ")
