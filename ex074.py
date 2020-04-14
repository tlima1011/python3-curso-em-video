from random import randint
#São cinco caracteres de 0 a 5
i = maior = menor = 0
nums = []
for i in range(0, 5):
    nums.append(randint(0, 10))
numeros = tuple(nums)
print(f'Números sorteados: ',end='')
for n in numeros:
    print(f'{n}', end=' ')

print(f'\nMaior número sorteado é {max(numeros)}')
print(f'Menor número sorteado é {min(numeros)}')




