from validadores import leiaInt
soma = 0
cp = 0
numeros = []
for i in range(1, 7):
    numero = leiaInt(f'Informe o {i}º número inteiro.: ')
    numeros += [numero]
    if numero % 2 == 0:
        soma += numero
        cp += 1
print(f'A soma dos números pares é {soma}\nQuantidade de números pares digitados: {cp}')
print('Os números pares:')
for i in range(0, 6):
    if numeros[i] % 2 == 0:
        print(f'O número {numeros[i]} está no posição [{i}]')

