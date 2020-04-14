def ehPrimo(numero):
    tot = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            print('\033[33m', end='')
            tot += 1
        else:
            print('\033[31m', end='')
        print('{} '.format(i), end='')
    if tot == 2:
        primo = 'é primo'
    else:
        primo = 'não é primo'
    return ('\n\033[0;30mO número {} foi divísivel {} vezes\nO número {}'.format( numero, tot, primo ))

print('NÚMEROS PRIMOS!!!')
numero = int(input('Informe um número.: '))
print(ehPrimo(numero))