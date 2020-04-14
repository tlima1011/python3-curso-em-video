from ex044_pagamentos import vista_dinheiro, cartao_vista, cartao_2x, cartao_3x_mais

print('{:=^40}'.format('\033[1;35mLOJÃO DO BRÁS\033[m'))
invalido = True
valor = float(input('\033[1;34mValor da compra R$\033[m'))
while invalido == True:
    condicao = input('''\033[1;34mInforme a condição de Pagamento:
[ 1 ] - À vista com dinheiro ou cheque
[ 2 ] - Cartão à vista
[ 3 ] - Cartão em 2 vezes
[ 4 ] - Cartão em 3 vezes ou mais\nOpção:\033[m''')
    if condicao == '1':
        print(vista_dinheiro(valor))
        invalido = False
    elif condicao == '2':
        print(cartao_vista(valor))
        invalido = False
    elif condicao == '3':
        print(cartao_2x(valor))
        invalido = False
    elif condicao == '4':
        print(cartao_3x_mais(valor))
        invalido = False
    else:
        print('\033[1;31mInválido, tente novamente\033[m')
        invalido = True