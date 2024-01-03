from time import sleep

def linha(msg,cor):
    tam = len(msg)
    print(cor)
    print("~" * int(tam+4))
    print(f"  {msg}")
    print("~" * int(tam+4))
    sleep(1)

    
def ajuda(lib,cor):
    print(cor)
    print(help(lib))
    sleep(1)


while True: 
    linha("SISTEMA DE AJUDAS PyHELP","\033[1;32m")
    lib = input("\033[0mFunção ou Biblioteca > ")
    if lib.upper() == "FIM":
        linha("ATÉ LOGO!","\033[1;31m")
        break
    else:
        linha(f"Acessando o manual do comando '{lib}' ","\033[1;36m")
        ajuda(lib,"\033[1;97m]")
