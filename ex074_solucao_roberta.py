from random import sample
numeros = tuple(sample(range(10), 5))
print(f'Os números sorteados são {numeros}\nO maior número: {max(numeros)}\nO menor número {min(numeros)}')
