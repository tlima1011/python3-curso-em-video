def somar(n1, n2):
    return f'{n1} + {n2} = {n1 + n2}'


def subtrair(n1, n2):
    return f'{n1} - {n2} = {n1 - n2}'


def multiplicar(n1, n2):
    return f'{n1} X {n2} = {n1 * n2}'


def dividir(n1, n2):
    return f'{n1} / {n2} = {n1 / n2:.2f}'


def divisaoInt(n1, n2):
    return f'{n1} // {n2} = {n1 // n2}'


def exponenciacao(n1, n2):
    return f'{n1} elevado a(o) {n2} = {n1 ** n2}'


def maior(n1, n2):
    if n1 == n2:
        return f'N1 - {n1} e N2 - {n2} são iguais'
    elif n1 > n2:
        return f'N1 - {n1} é maior que N2 - {n2}'
    else:
        return f'N2 - {n2} é maior que N1 - {n1}'


def menor(n1, n2):
    if n1 == n2:
        return f'N1 - {n1} e N2 - {n2} são iguais'
    elif n1 < n2:
        return f'N1 - {n1} é menor que N2 - {n2}'
    else:
        return f'N2 - {n2} é menor que N1 - {n1}'
