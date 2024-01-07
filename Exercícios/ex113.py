def leiaInt(msg):
    while True:
        try:
            num = int(input(f"\033[1;97m{msg}"))
        except KeyboardInterrupt:
            print("\033[1;31m O usuario não preferiu digitar o número.")
        except:
            print(f'\033[1;31mERRO! Por favor digite um número inteiro válido.')
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(f"\033[1;97m{msg}"))
        except KeyboardInterrupt:
            print("\033[1;31m O usuario não preferiu digitar o número.")
        except:
            print("\033[1;31mERRO! Por favor digite um número real válido.")
        else:
            return num

ni = leiaInt('Número inteiro: ')
nf = leiaFloat('Número Real: ')
print(f"O valor inteiro digitado foi {ni} e o real {nf}")
