from conversores_moedas import  convRealDolar, convDolarReal, convRealEuro, convEuroReal
tipoConversao = input('=' * 50 + '\nInforme o tipo de conversão: '
                                 '\n[ 1 ] - [ R$ / US$ ] - Real para Dólar '
                                 '\n[ 2 ] - [ US$ / R$ ] - Dólar para Real'
                                 '\n[ 3 ] - [ R$ / €] - Real para Euro'
                                 '\n[ 4 ] - [ € / R$] - Euro para Real'
                                 '\n[ 5 ] - Sair\n'
                                 + '=' * 50+'\nOpção.: ')
if tipoConversao == '1':
    real = float(input('Quantos reais possui.: R$'))
    print(convRealDolar(real))
elif tipoConversao == '2':
    dolar = float(input('Quantos dolares possui.: US$'))
    print(convDolarReal(dolar))
elif tipoConversao == '3':
    real = float(input('Quantos reais possui.: R$'))
    print(convRealEuro(real))
elif tipoConversao == '4':
    euro = float(input('Quantos euros possui.: €'))
    print(convEuroReal(euro))
elif tipoConversao == '5':
    SystemExit
else:
    print('Inválido')
print('Até Logo')

