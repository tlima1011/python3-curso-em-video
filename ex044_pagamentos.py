def vista_dinheiro(valor):
    valor_novo = valor - (valor * 0.10)
    return f'\n\033[1;34mValor à Vista com dinheiro ou cheque\nPreço Normal R${valor:.2f}\nDesconto {0.10 * 100:.2f}%\nNovo Valor R${valor_novo:.2f}\033[m'


def cartao_vista(valor):
    valor_novo = valor - (valor * 0.05)
    return f'\n\033[1;34mValor à Vista com cartão\nPreço Normal R${valor:.2f}\nDesconto {0.05 * 100:.2f}%\nNovo Valor R${ valor_novo:.2f}\033[m'


def cartao_2x(valor):
    return f'\n\033[1;34mCartão em 2X\nPreço Normal R${valor:.2f},\nPreço parcelado em 2X R${valor / 2:.2f}\033[m'


def cartao_3x_mais(valor):
    parcelas = int(input('Quantas parcelas?\n'))
    valor_novo = valor + (valor * 0.20)
    valor_parcelado = valor_novo / parcelas
    return f'\n\033[1;34mValor Parcelado com cartão - {parcelas}X de R${valor_parcelado:.2f}' \
           f'\nPreço Normal R${valor:.2f}\nJuros {0.20 * 100:.2f}%\n' \
           f'Novo Valor R${valor_novo:.2f}\033[m'