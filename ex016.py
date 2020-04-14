from math import trunc


def conversaoInterio(n):
    return f'A parte inteira de {n} é {trunc(n)} '


numero = float(input('Informe um número.: '))
print(conversaoInterio(numero))
