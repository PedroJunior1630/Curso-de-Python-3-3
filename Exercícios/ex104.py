def leiaInt(msgInput):
    while True:
        num = input(f"\033[1;97m{msgInput}")
        if num.isnumeric() == True:
            break
        else:
            print(f"\033[1;31mERRO o valor digitado não é um número!")
    return int(num)

n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}")
