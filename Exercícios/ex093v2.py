dicionario =  {}
lista = [[],[]]
goals = assistances = 0
print("=+=" * 20)
print(f"{'UEFA CHAMPIONS LEAGUE SCORED':^10}")
print("=+=" * 20)
dicionario["Name"] = str(input('Player Name: ')).title().strip()
dicionario["Season"] = str(input('Which season: '))
dicionario["Matches"] = int(input('How many games did play: '))
for i in range(0,dicionario["Matches"]):
    lista[0].append(int(input(f'{i+1}° Match did score: ')))
    lista[1].append(int(input(f'{i+1}° Match did assistance: ')))
    goals += lista[0][i]
    assistances += lista[1][i]
ga = goals + assistances
dicionario["Goals"] = lista[0]
dicionario["Assistances"] = lista[1]
dicionario["TotalGoals"] = goals
dicionario["TotalAssistances"] = assistances
print("=+=" * 20)
print(f'{dicionario["Name"]} in Champions League {dicionario["Season"]}')
print(f'Played {dicionario["Matches"]} matches')
print(f'Scored {dicionario["TotalGoals"]} goals.')
print(f'Assistances: {dicionario["TotalAssistances"]}')
print(f'Goal Average: {dicionario["TotalGoals"] / dicionario["Matches"]:.2f}')
print(f'G/A Average: {ga / dicionario["Matches"]:.2f}')
print(f'G+A: {ga}')
print("=+=" * 20)
print(dicionario)
