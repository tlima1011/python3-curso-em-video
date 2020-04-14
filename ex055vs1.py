from validadores import leiaReal
maior = menor = 0
for i in range(1, 6):
    peso = leiaReal(f'Peso da {i}ª pessoa: ')
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O mais pesado {maior}Kg\nO mais leve é {menor}Kg')
