def maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return f'O número {n1} é maior'
    elif n2 > n1 and n2 > n3:
        return f'O número {n2} é maior'
    else:
        return f'O número {n3} é maior'


def menor(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return f'O número {n1} é menor'
    elif n2 < n1 and n2 < n3:
        return f'O número {n2} é menor'
    else:
        return f'O número {n3} é menor'