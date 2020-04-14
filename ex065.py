from validadores import leiaInt
from ex064_pkg_list import listar
continuar = 's'
media = maior = soma = menor = i = 0
numeros = []
while continuar in 'Ss':
    i += 1
    numero = leiaInt(f'Digite o {i}º número: ')
    soma += numero
    numeros.append(numero)
    if i == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = input('Deseja continuar [S/N]: '.strip().upper())[0]

print(listar(numeros))
media = soma / i
print(f'Média dos números: {media:.1f}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
print(f'Soma: {soma}')
print(f'Quantidade de números digitados: {len(numeros)}')

