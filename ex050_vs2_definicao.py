from random import randint


def definicao(inicial, final, inicio, termino):
    cp = ci = somaImpar = soma = somaPar = 0
    pares = []
    impares = []
    for inicial in range(inicial, final):
        numero = randint(inicio, termino)
        soma += numero
        #print(numero, end=' ')
        if numero % 2 == 0:
            somaPar += numero
            pares = pares + [numero]
            cp += 1
        else:
            somaImpar += numero
            impares = impares + [numero]
            ci += 1
        pares = f'\nA soma dos números pares é {somaPar}\nQuantidade de números pares: {cp}'
        impares = f'\nA soma dos números impares é {somaImpar}\nQuantidade de números impares: {ci}'
        return pares + impares
