from time import sleep
c = ('\033[m',          #0 - sem cores
     '\033[0;30;41m',   #1 - vermelho
     '\033[0;30;42m',   #2 - verde
     '\033[0;30;43m',   #3 - amarelo
     '\033[0;30;44m',   #4 - azul
     '\033[0;30;45m',   #5 - roxo
     '\033[7;30m'       #6 - Branco
     )


def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    print(c[6], end='')
    help(comando)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(F'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#Programa Principal
comando = ''
while True:
    titulo('SISTEM DE AJUDA PyHELP', 3)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando.lower())
titulo('ATÉ LOGO ', 1)