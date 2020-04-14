from validadores import leiaReal
menor = 999999999
maior = 0
for i in range(1, 6):
    peso = leiaReal(f'Informe o peso da {i}ª pessoa: ')
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O mais pesado é {}Kg\nMais Leve é {}Kg'.format(maior, menor))
