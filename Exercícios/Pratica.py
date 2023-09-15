lanche = ('Pudim', 'Café', 'Pizza', 'Hamburger')
print(lanche[0:3]) #vai pegar o indíce 0 que é o Pudim até a Pizza or que o último número é excluido.
print(lanche[1:]) #vai pegar do café e vai até o final pois não foi especificado.
print(lanche[-1]) #vai pegar o último item da lista e assim por diante: -2 o antepenúltimo, -3...

for c in lanche: #possivel usar estrutura de repetição
    print(c) #vai imprimir todos os itens da lista

print(sorted(lanche))

print(enumerate(lanche))

print(lanche.index('Pizza'))

print(c in lanche)
