from distancias import metros_centimetros, metros_centimetros, metros_milimetros, centimetros_metros, milimetros_metros, metros_hectometros, metros_decametros, metros_kilometros, decametros_metros, hectometros_metros, kilometros_metros
from validadores import leiaInt, leiaReal

print('=' * 30 + '\nInformação de medidas')
opcao = input('''
Informe a conversão de metragrem
[ 1 ] - Metros para centimetros
[ 2 ] - Metros para milimetros
[ 3 ] - Centimetros para metros
[ 4 ] - Milimetros para metros
[ 5 ] - Metros para decametros
[ 6 ] - Metros para hectometros
[ 7 ] - Metros para kilometros
[ 8 ] - decâmetros para metros
[ 9 ] - hectometros para metros
[ 10 ] - kilômetros para metros \nOpção: ''')
if opcao == '1':
    metros = leiaReal('Informe o valor em metros.: ')
    print(metros_centimetros(metros))
elif opcao == '2':
    metros = leiaReal( 'Informe o valor em metros.: ')
    print(metros_milimetros(metros))
elif opcao == '3':
    cm = leiaReal('Informe o valor em centimetros.: ')
    print(centimetros_metros(cm))
elif opcao == '4':
    mm = leiaReal('Informe o valor em milimetros.: ')
    print(milimetros_metros(mm))
elif opcao == '5':
    m = leiaReal('Informe o valor em metros.: ')
    print(metros_decametros(m))
elif opcao == '6':
    m = leiaReal('Informe o valor em metros.: ')
    print(metros_hectometros(m))
elif opcao == '7':
    m = leiaReal('Informe o valor em metros.: ')
    print(metros_kilometros(m))
elif opcao == '8':
    dm = leiaReal('Informe o valor em decametros.: ')
    print(decametros_metros(dm))
elif opcao == '9':
    hm = leiaReal('Informe o valor em hectômetros.: ')
    print(hectometros_metros(hm))
elif opcao == '10':
    km = leiaReal('Informe o valor em kilometros.: ')
    print(kilometros_metros(km))
else:
    print('Inválido')

