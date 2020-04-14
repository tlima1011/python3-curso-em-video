from random import randint
from time import sleep
from validadores import leiaInt
print('-=' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 30)
total = vitoria = 0
while True:
    num_cpu = randint(1, 10)
    num_player = leiaInt('DIGA UM VALOR.: ')
    par_impar_player = ' '
    while par_impar_player not in 'PI':
        par_impar_player = input('PAR OU IMPAR [P/I]: ').strip().upper()[0]
    if par_impar_player == 'P':
        par_impar_cpu = 'I'
    else:
        par_impar_cpu = 'P'
    total = num_player + num_cpu
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print('Processando...')
    sleep(1)
    if par_impar_player == resultado[0]:
        print(f'Você jogou no {num_player} e o CPU {num_cpu} com Total =  {total} e DEU {resultado}')
        print('\033[1;34mVOCÊ VENCEU e vamos jogar novamente...\033[m')
        vitoria += 1
    else:
        print( f'Você jogou no {num_player} e o CPU {num_cpu} com Total = {total} e DEU {resultado}' )
        print('\033[1;31mSE FUDEU\033[m')
        break
print('\033[1;31m---GAME OVER---\033[m')
print(f'Você Venceu {vitoria} vezes')