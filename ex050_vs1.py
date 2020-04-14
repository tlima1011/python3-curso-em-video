from random import randint
from validadores import leiaInt
soma = 0
cp = 0
numeros = []
inicial = leiaInt('Informe o número inicial.: ')
final = leiaInt('Informe o número final.: ')
inicio = leiaInt('Valor inicial.: ')
termino = leiaInt('Valor final.: ')
#randint(0,2)
for inicial in range(inicial, final):
    numero = randint(inicio, termino)
    numeros = numeros + [numero]
    print(numero, end=' ')
    if numero % 2 == 0:
        soma += numero
        cp += 1
print('\nA soma dos números pares é {}\nQuantidade de números pares digitados: {}' .format(soma, cp))
#print(numeros[0])
print('Os números pares:')
for i in range(0, 6):
    if numeros[i] % 2 == 0:
        print('O número {} está no posição [{}]'.format(numeros[i], i))