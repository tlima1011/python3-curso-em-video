def dobro(preco=0):
    res = preco * 2
    return res


def metade(preco=0):
    res = preco / 2
    return res


def aumentar(preco=0, tx=0):
    res = preco + (preco * (tx / 100))
    return res


def diminuir(preco=0, tx=0):
    res = preco - (preco * (tx / 100))
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

