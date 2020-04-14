from ex059_calculadora import somar, subtrair, multiplicar, dividir, divisaoInt, exponenciacao, maior, menor
from validadores import leiaInt
opcao = ''
print('\033[1;33m<----------<<< CALCULADORA V.3.0 >>>-------------->\033[m')
numero1 = leiaInt('Número 1: ')
numero2 = leiaInt('Número 2: ')
while opcao != '10':
    opcao = input('''\033[1;36mINFORME O TIPO DA OPERAÇÃO
[ 1 ] - SOMAR
[ 2 ] - SUBTRAIR 
[ 3 ] - MULTIPLICAR 
[ 4 ] - DIVIDIR 
[ 5 ] - DIVISÃO INTEIRA 
[ 6 ] - EXPONENCIAÇÃO 
[ 7 ] - MAIOR
[ 8 ] - MENOR
[ 9 ] - NOVOS NÚMEROS 
[ 10 ] - SAIR DO PROGRAMA
OPÇÃO: \033[m''')
    opcao = opcao.strip()
    if opcao == '1':
        print(somar(numero1, numero2))
    elif opcao == '2':
        print(subtrair(numero1, numero2))
    elif opcao == '3':
        print(multiplicar(numero1, numero2))
    elif opcao == '4':
        print(dividir(numero1, numero2))
    elif opcao == '5':
        print(divisaoInt(numero1, numero2))
    elif opcao == '6':
        print(exponenciacao(numero1, numero2))
    elif opcao == '7':
        print(maior(numero1, numero2))
    elif opcao == '8':
        print(menor(numero1, numero2))
    elif opcao == '9':
        print('Novos Nùmeros a serem digitados...')
        numero1 = leiaInt('Número 1: ')
        numero2 = leiaInt('Número 2: ')
    elif opcao == '10':
        print('Saindo do programa')
        break
    else:
        print('Opção inválida...tente novamente')
print('Bye...')




