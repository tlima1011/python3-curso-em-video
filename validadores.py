def leiaInt(msg):
    """
    -> Validador de valores como inteiro
    :param msg: entrada de uma string dada pelo usuário
    :return: o retorno do valor sendo como inteiro
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mSaída dada pelo usuário!!!\033[m')
            return 0
        return n


def leiaReal(msg1):
    """
    -> Validador de número real
    :param msg1: Valor de entrada pleo usuário
    :return: retornar como número real
    """
    while True:
        try:
            num = float(input(msg1))
        except (ValueError, TypeError):
            print('\033[31mValor incorreto, digite um número real válido!!!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mSaída dada pelo usuário!!!\033[m')
            return 0
        return num


def leiaSexo(msg):
    sexo = str(msg).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input( 'Informe o sexo [M/F]: ' ).upper().strip() )[0]
        if sexo not in 'MF':
            print( '\033[1;31mInválido digite novamente!!! Necessário ser [M / F] - Try again\033[m' )

