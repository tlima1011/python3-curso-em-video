def convCf(c):
    f = c * (9 / 5) + 32
    return f'{c:.1f}ºC = {f:.1f}ºF '


def convFc(f):
    c = (f - 32) * (5 / 9)
    return f'{f:.1f}ºF = {c:.1f}ºC '


def convCk(c):
    k = 273.15 + c
    return f'{c:.1f}Cº = {k:.2f}K '


def convKc(k):
    c = k - 273.15
    return f'{k:.1f}ºK = {c:.2f}ºC '


def convKf(k):
    f = (k - 273.15) * (9 / 5) + 32
    return f'{k:.1f}ºK = {f:.2f}ºF '


def convFk(f):
    k = (f - 32) * (5 / 9) + 273.15
    return f'{f:.1f}ºF = {k:.2f}ºK '