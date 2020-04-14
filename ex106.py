from time import sleep


def cabecalho():
    txt = 'SISTEMA DE AJUDA PyHELP'
    tam = len(txt) + 4
    print('\033[1;36;43m~' * tam)
    print(f'\033[1;36;43m  {txt}  ')
    print('\033[1;36;43m~\033[m' * tam)


def funcao_bibioteca(t):
    texto = 'Acessando o manual do comando'
    tam = len(texto) + len( t ) + 6
    sleep(1)
    print('\033[1;30;44m~' * tam)
    print(f'\033[1;30;44m {texto} "{t}"')
    print('\033[1;30;44m~' * tam)
    sleep(1)
    ajuda = f'\033[7;31;40m {help(t)}'
    return ajuda


def fim():
    texto = 'Até Logo'
    tam = len(texto) + 4
    sleep(1)
    print('\033[1;30;41m~' * tam)
    print(f'\033[1;30;41m  {texto}  ')
    print('\033[1;30;41m~' * tam)
    sleep(1)


while True:
    cabecalho()
    t = str(input('Função ou Biblioteca: ')).strip().lower()
    if t.upper() == 'FIM':
        fim()
        break
    else:
        funcao_bibioteca(t)