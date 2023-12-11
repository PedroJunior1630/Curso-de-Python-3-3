matriz = [[], [], []]
c1 = c2 = 0
for num in range(1,10):
    if num >= 1 and num <= 3:
        c1 = 0 
        matriz[0].append(int(input(f'Digite um número para a posição [{c1}][{num-1}]: ')))
    if num >= 4 and num <= 6:
        c1 = 1
        matriz[1].append(int(input(f'Digite um número para a posição [{c1}][{num-4}]: ')))
    if num >= 7 and num <= 9:
        c1 = 2
        matriz[2].append(int(input(f'Digite um número para a posição [{c1}][{num-7}]: ')))
for m in matriz[0]:
    c2 += 1
    print(f"[ {m} ]",end =" ")
    if c2 == 3:
        print("\n",end = "")
        for m in matriz[1]:
            c2 += 1
            print(f"[ {m} ]",end = " ")
            if c2 == 6:
                print("\n",end = "")
                for m in matriz[2]:
                    print(f"[ {m} ]",end = " ")
