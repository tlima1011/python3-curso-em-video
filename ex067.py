titulo = 'TABUADA VS 3.0'
print(f'{titulo:=^30}')
while True:
    tab = int(input('Informe a tabuada: '))
    if tab < 0:
        break
    print('-=' * 10)
    print(f'TABUADA DE {tab}')
    print('-=' * 10)
    for i in range(1, 11):
        print(f'{tab} x {i} = {tab * i}')
    print('-=' * 10)
print('PROGRAMA ENCERRADO!!!')

