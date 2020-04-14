from random import randint
from time import sleep
import emoji


def jogo(v):
    if v == 1:
        player = emoji.emojize('Pedra :punch:', use_aliases=True)
    elif v == 2:
        player = emoji.emojize('Papel :page_facing_up: ', use_aliases=True)
    else:
        player = emoji.emojize('Tesoura :scissors:)', use_aliases=True)
    cpu = randint(1, 3)
    if cpu == 1:
        peca = emoji.emojize('Pedra :punch:', use_aliases=True)
    elif cpu == 2:
        peca = emoji.emojize('Papel :page_facing_up: ', use_aliases=True)
    else:
        peca = emoji.emojize('Tesoura :scissors:)', use_aliases=True)
    print('\033[1;31mJO\033[m')
    sleep(0.7)
    print('\033[1;33mKEN\033[m')
    sleep(0.7)
    print('\033[1;32mPÔ\033[m')
    sleep(0.7)
    if v == cpu:
        return f'\033[1;36mDeu Empate, minha escolha {peca} e sua {player} !!! \033[m'
    elif cpu == 1 and v == 3:
        return f'\033[1;31mEu ganhei com {peca} e você com {player}\033[m'
    elif v == 1 and cpu == 3:
        return f'\033[1;34mEu ´perdi com {peca} e você com {player}\033[m'
    elif v == 2 and cpu == 3:
        return f'\033[1;34m\033[1;31mEu ganhei com {peca} e você com {player} \033[m'
    elif v == 3 and cpu == 2:
        return f'\033[1;34mEu perdi com {peca} e você com {player}\033[m '
    elif v == 1 and cpu == 2:
        return f'\033[1;31mEu ganhei com {peca} e você com {player} \033[m'
    else:
        return f'\033[1;34mEu perdi com {peca} e você com {player} \033[m'
