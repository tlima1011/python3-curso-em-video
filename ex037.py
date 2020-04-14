from ex037_conversores_numeros import convHex, convBin, convOctal
numero = int(input('Informe um número.: '))
valido = True
while valido == True:
    conversao = input('''\033[1;33m<----- CONVERSÃO DE NÚMEROS ----->'
[ 1 ] - De número para binário 
[ 2 ] - De número para octal
[ 3 ] - De número para hexadecimal
[ 4 ] - Sair
[ 5 ] - Outro número\nOpçao.: \033[m''')
    if conversao == '1':
        print(convBin(numero))
        #invalido = False
    elif conversao == '2':
        print(convOctal(numero))
        #invalido = False
    elif conversao == '3':
        print(convHex(numero))
        #invalido = False
    elif conversao == '4':
        valido = False
    elif conversao == '5':
        numero = int(input('Escolha outro  número.: '))
    else:
        print('\033[1;31mInválido e informe a conversão correta\033[m')
        valido = True
print('Até Logo')