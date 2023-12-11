num = list()

for numeros in range(0,7):
    num.append(int(input('Digite um número: ')))
num.sort()
print(f"Números pares: ",end = " ")
for par in num:
    if par % 2 == 0:
        print(par,end =" ")
print(f"\nNúmeros impares: ",end = " ")
for imp in num:
    if imp % 2 == 1:
        print(imp,end = " ")
