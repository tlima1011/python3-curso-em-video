from ex060_fatoriais import while_fatorial, for_fatorial
from validadores import leiaInt
opcao = 0
while opcao != '4':
    print('**** FATORIAL **** ')
    numero = leiaInt('Informe o número para fatorial.: ')
    opcao = input('''Informe qual fatorial
[ 1 ] - FATORIAL COM WHILE 
[ 2 ] - FATORIAL COM FOR 
[ 3 ] - COLOCAR OUTRO NÚMERO
[ 4 ] - SAIR
OPÇÃO.: ''')
    if opcao == '1':
        print(while_fatorial(numero))
    elif opcao == '2':
        print(for_fatorial(numero))
    elif opcao == '3':
        print('Coloque novamente o valor')
    elif opcao == '4':
        print('Saindo do programa!!!')
    else:
        print('Inválido digite novamente')
print('TENHA UM BOM DIA!!!')

