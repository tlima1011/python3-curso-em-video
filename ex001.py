def olaMundo():
    print('Olá mundo')


def olaMundo2(msg):
    """
    :date: 31/03/2020
    :param msg: Recebe o parâmetro em forma de texto
    :return: Retorna a mensagem que deu a entrada
    """
    return f'A mensagem é {msg} '


print('\033[1;31mOlá mundo\033[m')
olaMundo()


msg = 'Olá mundo'
print(msg)
help(olaMundo2)

#print('\033[7;33;44mOlá, Mundo\033[m')