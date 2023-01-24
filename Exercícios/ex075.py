num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num3 = int(input('Digite o 3° número: '))
num4 = int(input('Digite o 4° número: '))

numeros = (num1,num2,num3,num4)
print(f'O número 9 apareceu: {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu  pela primeira vez na: {numeros.index(3) + 1}° posição')
else:
    print('O número 3 não foi digitado')
c = 0
print('Numeros pares: ',end = "")
for n in numeros:
    if n % 2 == 0:
        print(n,end = " ")
