titulo = 'TABUADA VS 3.0'
print(f'{titulo:=^30}')
inicia = final = 0
while True:
    tab = int(input('Informe a tabuada: '))
    if tab < 0:
        break
    inicia = int(input( 'Começa com qual número? '))
    final = int(input( 'Termina com qual número? '))
    while inicia > final:
        if inicia > final:
            print('Inválido, o início não pode ser maior que final')
            inicia = int( input('Começa com qual número? '))
            final = int( input('Termina com qual número? '))
        else:
            print('-=' * 10)
            print(f'TABUADA DE {tab}')
            print('-=' * 10)
            for i in range(inicia, final+1):
                print(f'{tab} x {i} = {tab * i}')
print('PROGRAMA ENCERRADO!!!')