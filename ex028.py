from random import randint
from time import sleep


def resultado(n):
    escolhido = randint(0, 5)
    print('Processando...')
    sleep(3)
    if numero == escolhido:
        return f'Você ganhou!!!, número do CPU = {escolhido} e o seu = {n}'
    else:
        return f'Você perdeu!!!, número do CPU = {escolhido} e o seu = {n}'


print('-=-' * 40)
numero = int(input('Informe um coloque um número de 0 a 5: \n'))
print(resultado(numero))


