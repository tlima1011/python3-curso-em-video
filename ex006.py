def resultados(n):
    dobro = n * 2
    triplo = n * 3
    raizQuadrada = n ** 0.5
    return f'O dobro de {n} é {dobro}:\nO triplo é = {triplo}\nRaiz Quadrada de {raizQuadrada:.2f}'


numero = int(input('Informe um número.: '))
print(resultados(numero))