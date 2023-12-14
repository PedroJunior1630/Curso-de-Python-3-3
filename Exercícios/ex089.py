nome_notas = []
boletim = []
while True:
    print("=+=" * 20)
    nome_notas.append(input('Nome: '))
    nome_notas.append(float(input('1° Nota: ')))
    nome_notas.append(float(input('2° Nota: ')))
    boletim.append(nome_notas[:])
    nome_notas.clear()
    opc = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if "N" in opc:
        break
media = []
c = 0
print("=+=" * 20)
print("N°      Nome           Média")
print("=+=" * 20)
for aluno in boletim:
    md = (aluno[1] + aluno[2]) / 2
    media.append(md)
    print(f'{c} {aluno[0]:>10} {media[c]:^25}')
    md = 0
    c += 1
print("=+=" * 20)
while True:
    al = int(input('Digite qual aluno deseja ver?(999 para condição de parada): '))
    if al == 999:
        break
    else:
        print(f'Aluno {boletim[al][0]} teve as notas [{boletim[al][1]}] [{boletim[al][2]}]')
