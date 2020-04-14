from validadores import leiaInt
numeros = list()
cont = ''
while True:
    num = leiaInt('Digite um número.: ')
    while num in numeros:
        print('Valor Duplicado!!!, digite novamente o número!!!')
        num = leiaInt('Digite outro número diferente.: ')
    print('Valor adicionado com sucesso!!!')
    numeros.append(num)
    cont = str(input('Deseja continuar [S/N]')).upper().strip()[0]
    if cont == 'N':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')
