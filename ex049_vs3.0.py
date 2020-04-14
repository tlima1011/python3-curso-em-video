from validadores import leiaInt
numInicial = 0
numFinal = 0
inicio = 0
final = 0
validos = True
print('\033[1;36m=\033[m' * 15
        +'\n\033[1;36mTABUADA VS 3.0\033[m')
print('\033[1;36m=\033[m' * 15)
while validos == True:
    numInicial = leiaInt('O início da tabuada.: ')
    numFinal = leiaInt('Final da tabuada.: ')
    if numFinal < numInicial:
        print('O final da tabuada não pode ser maior')
        validos = True
    else:
        validos = False
val = True
while val == True:
    inicio = leiaInt('Começa com qual número.: ')
    final = leiaInt('Termina com qual número.: ')
    if final < inicio:
        print('O número final não pode ser maior')
        val = True
    else:
        val = False
print(f'''
Inicia com: {numInicial}
Termina com: {numFinal}
Inicia com: {inicio}
Termina com: {final}
''')
for numInicial in range(numInicial, numFinal+1):
    print('\033[1;36m=\033[m' * 15 +f'\n\033[1;36mTABUADA DE: {numInicial}\033[m')
    print('\033[1;36m=\033[m' * 15)
    for i in range(inicio, final+1):
        print(f'\033[1;33m{numInicial} x {i:2} = {numInicial * i}\033[m')
