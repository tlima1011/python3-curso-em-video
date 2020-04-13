def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def aumentar(preco=0, tx=0, formato=False):
    res = preco + (preco * (tx / 100))
    return res if formato is False else moeda(res)


def diminuir(preco=0, tx=0, formato=False):
    res = preco - (preco * (tx / 100))
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco = 0, taxa = 10, taxar = 10):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do Preço: \t{dobro(preco,True)}')
    print(f'Metade do Preço: \t{metade(preco, True)}')
    print(f'Aumento de {taxa}%: \t{aumentar(preco,taxa,True)}')
    print(f'Redução de {taxar}%: \t{diminuir(preco, taxar, True )}')
    print( '-' * 30 )