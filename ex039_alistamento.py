from datetime import date


def alistamento(a):
    anoHoje = date.today().year
    idade = anoHoje - a
    if idade == 18:
        return f'Está na época de alistamento com {idade} anos'
    elif idade > 18:
        saldo = 18 - idade
        return f'Passou do dia de alistameno com {idade} anos, você deveria ter se alistado há {saldo} anos\nE seu alistamento em {anoHoje + saldo}'
    else:
        saldo = idade - 18
        return f'Com a idade de {idade} anos ainda não é hora, ainda falta {saldo} anos para alistamento\nSeu alistamento em {a - saldo}'