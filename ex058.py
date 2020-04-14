from random import randint
from time import sleep
from validadores import leiaInt
vezes = 0
num_player = 1
nome = input('Coloquei seu nome.: ')
print('Olá, {}, eu quero jogar um jogo'.format(nome).strip().title())
print('\033[1;32m-=-\033[m' * 40)
num_cpu = randint(0, 10)
print('Vamos jogar um jogo !!!')
while num_player != num_cpu:
    num_player = leiaInt('Pense em um número de 0 a 10, eu já pensei!\n')
    print('\033[1;32mProcessando...\033[m')
    sleep(0.3)
    if num_player != num_cpu:
        vezes += 1
        if num_player > num_cpu:
            print('Perdeu, tente novamente, porém é menos...')
        else:
            print('Perdeu, tente novamente, porém é mais...')

print(f'Você Acertou o Número - Placar Eu \033[1;32m[{num_cpu}]\033[m - Você \033[1;31m[{num_player}]\033[m!!!')
print(f'Foram neceessário {vezes} vezes para Acertar')
