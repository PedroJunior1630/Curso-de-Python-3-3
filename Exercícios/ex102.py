import math
def fatorial(num, cal = False):
    fact = 1
    if cal == True:
        for c in range(num,0,-1):
            print(f'{c}',end = " ")
            fact *= c
            if c == 1:
                print("=",end=" ")
            else:
                print("x",end=" ")
        return fact
    else:
        return math.factorial(num)
res = fatorial(6, True)
print(res)
