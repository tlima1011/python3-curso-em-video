numeros = []
from random import randint

for i in range(0, 6):
    numeros.append(randint(1, 10))

for i, v in enumerate(numeros):
    print(f'{i} com valor {v}')
