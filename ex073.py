times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Forteleza',
         'Goiás', 'Bahia', 'Vasco', 'Atlètico-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', "Avaí")
#Exercício A:
print(f'Os cinco primeiros colocados {times[:5]}')
#Wxercício B
print(f'Os 4 últimos {times[-4:]}')
#Colocando em ordem alfabética
ordem = sorted(times)
print('TIMES EM ORDEM ALFABÉTICA: ')
for time in ordem:
   print(time)
print('CLASSIFICAÇÃO BRASILEIRO - 2019')
for c in range(0, len(times)):
    print(f'{c+1}º: {times[c]}')

procura_time = input('Que time deseja procurar.: ').title().strip()
print(f'O time {procura_time} está na posição: {times.index(procura_time)}')
