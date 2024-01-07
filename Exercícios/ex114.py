import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print("Site pudim não está acessível no momento.")
else:
    print("Site pudim acessado com sucesso!")
