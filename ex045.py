from random import randint
from time import sleep
import emoji
from ex045_joken import jogo


print('\033[1;32m<========== BEM VINDO AO JOKENPÔ ==========>')
nome = input('Informe o seu nome.: ').strip()
print(f'Olá, {nome.upper()}, eu quero jogar um jogo')
print('Eu já esoolhi agora você escolhe!!!')
objeto = int(input(emoji.emojize('''Qual objeto 
[ 1 ] - Pedra - :punch:'
[ 2 ] - Papel - :page_facing_up:'
[ 3 ] - Tesoura - :scissors:\nOpção.: \033[m''', use_aliases=True)))
print(jogo(objeto))
