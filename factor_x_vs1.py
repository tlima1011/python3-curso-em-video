from math import factorial
def fatorial(inicial, final):
    for inicial in range(inicial, final+1):
        #f.append('O fatorial de {}! = {}'.format(inicial, factorial(inicial)))
        print(f'O fatorial de {inicial}! = {factorial(inicial)}')
    return True
inicial = int(input('Número Inicial: '))
final = int(input('Número Final: '))
print(fatorial(inicial, final))