def tabuada(numero):
    print('=' * 15 + f'\nTabuada de.: {numero}' )
    print('=' * 15)
    tabuada = ''
    for i in range(1, 11):
        print(f'\033[1;33m{numero} x {i:2} = {numero * i}\033[m')
    print('=' * 12)
    #return tabuada