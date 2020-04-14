from validadores import leiaInt
numeros = []
while True:
    numeros.append(leiaInt('Informe um número.: '))
    continuar = str(input('Quantos valores para continuar {S/N]').strip().upper()[0])
    if continuar == 'N':
        break

numeros.sort(reverse=True)
print(f'Quantidade de números digitados {len(numeros)}')
print(f'Números Ordenados de forma Decrescente: {numeros}')
if 5 in numeros:
    print(f'O número 5 encontrado na {numeros.index(5)+1}ª posição ')
else:
    print(f'O número 5 não foi encontrado')
