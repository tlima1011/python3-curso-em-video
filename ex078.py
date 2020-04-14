from validadores import leiaInt
maiores = list()
menores = list()
numeros = list()
menor = maior = c = 0
for i in range(0, 5):
    c += 1
    numeros.append(leiaInt(f'Informe o {c}º Número: '))

for i in range(0, len(numeros)):
    if numeros[i] == max(numeros):
        maiores.append(i+1)
    if numeros[i] == min(numeros):
        menores.append(i+1)
print(f'~' * 60)
print(f'Você digitou os valores... {numeros}')
print(f'Maiores números são {max(numeros)} nas posições... {maiores}')
print(f'Menor número digitado é {min(numeros)} nas posições... {menores}')
print(f'~' * 60)