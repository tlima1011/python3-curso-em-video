from validadores import leiaInt
pares = list()
impares = list()
nums = list()
continuar = ''
soma = somapares = somaimpares = 0
while True:
    nums.append(leiaInt('Informe um número.: '))
    continuar = str(input('Deseja continuar {S/N]').upper().strip()[0])
    if continuar == 'N':
        break

for i, v in enumerate(nums):
    soma += v
    if v % 2 == 0:
        pares.append(v)
        somapares += v
    else:
        impares.append(v)
        somaimpares += v

print(f'Lista de Números.: {nums} com {len(nums)} números digitados e a soma {soma}'
      f'\nLista de Pares.: {pares} com {len(pares)} números digitados e a soma dos pares {somapares}'
      f'\nLista de Impares.: {impares} com {len(impares)} números digitados e a soma dos impares {somaimpares}')
