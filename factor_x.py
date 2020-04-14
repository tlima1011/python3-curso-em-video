from math import factorial
def fatorial(n):
    return f'O fatorial de {n}! = {factorial(n)} '

numero = int(input('Número: '))
print(fatorial(numero))