def forma_triangulo(l1, l2, l3):
    existencia = True
    if (l1 < (l2 + l3)) and (l2 < (l1 + l3) and (l3 < (l1 + l2))):
        if ((l1 == l2) and (l2 == l3) and (l1 == l3)):
            tipo = '\033[1;33mEquilátero\033[m'
        elif ((l1 != l2) and (l2 != l3) and (l1 != l3)):
            tipo = '\033[1;33mEscaleno\033[m'
        else:
            tipo = '\033[1;33mIsósceles\033[m'
        return f'É um triângulo?\nResposta: {existencia} e é do tipo {tipo}'
    else:
        existencia = False
        return f'\033[1;31mÉ um triângulo ?\nResposta: {existencia}\033[m'