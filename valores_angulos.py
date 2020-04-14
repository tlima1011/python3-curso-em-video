from math import sin, cos, tan, radians


def valores(a):
    s = sin(radians(a))
    cosseno = cos(radians(a))
    tangente = tan(radians(a))
    return f'O ângulo de {a}º tem os seguintes valores:\nSeno = {s:.2f}\nCosseno = {cosseno:.2f}\nTangente = {tangente:.2f}'