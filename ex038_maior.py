from validadores import leiaInt


def maior(n1, n2):
    if n1 == n2:
        return f'O número n1 = {n1} e n2 = {n2} são iguais '
    elif n1 > n2:
        return f'O número n1 = {n1} é maior que n2 = {n2} '
    else:
        return f'O número n2 = {n2} é maior que n1 = {n1} '