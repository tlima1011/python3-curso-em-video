from time import sleep
from ex059_calculadora import somar, subtrair, multiplicar, maior
from validadores import leiaInt
opcao = '0'
n1 = leiaInt('Primeiro valor.: ')
n2 = leiaInt('Segundo valor.: ')
while opcao != '5':
    opcao = input('''[ 1 ] - Soma
[ 2 ] - Multiplicar 
[ 3 ] - Maior 
[ 4 ] - Novos Números
[ 5 ] - Sair do Programa 
Opção: ''')
if opcao == '1':
    print(somar(n1, n2))
elif opcao == '2':
    print(multiplicar(n1, n2))
elif opcao == '3':
    print(maior(n1, n2))
elif opcao == '4':
    print('Informe o números vovamente')
    n1 = leiaInt('Primeiro valor.: ')
    n2 = leiaInt('Segundo valor.: ')
elif opcao == '5':
    print('Saindo do programa...')
else:
    print('Tente novamente')
print('-=-' * 10)
sleep(2)
print('...FIM DO PROGRAMA...')








