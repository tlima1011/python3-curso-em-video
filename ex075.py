from validadores import leiaInt
nums = []
pares = []
posicao = contador = tot_par = 0
for i in range(0, 4):
    contador += 1
    nums.append(leiaInt(f'Digite o {contador} valor: '))
    if nums[i] % 2 == 0:
        pares.append(nums[i])
numeros = tuple(nums)
pares1 = tuple(pares)

print(f'Você digitou os valores {numeros}')
print(f'Valores pares digitados {pares1}')
if 3 in numeros:
    print(f'O valor 3 apareceu na posição {numeros.index(3)}')
else:
    print(f'Não foi encontrado o número 3')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')



