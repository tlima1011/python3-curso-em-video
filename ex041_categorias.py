from datetime import date


def categoria(n):
    anoHoje = date.today().year
    idade = anoHoje - n
    if idade <= 9:
        return f'Com a idade de {idade} anos está na categoria MIRIM'
    elif idade <= 14:
        return f'Com a idade de {idade} anos está na categoria INFANTIL'
    elif idade <= 19:
        return f'Com a idade de {idade} anos está na categoria JUNIOR'
    elif idade <= 20:
        return f'Com a idade de {idade} anos está na categoria SÊNIOR'
    else:
        return f'Com a idade de {idade} anos está na categoria MASTER'