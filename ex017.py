from math import hypot


def hipotenusa(ca, co):
    """hipotenusa = (math.pow(ca, 2)) + (math.pow(co, 2))
    h = math.sqrt(hipotenusa)"""
    h = hypot(ca, co)
    return f'Catato adjcaente = {ca}\nCateto oposto = {co}\nHipotenusa = {h:.2f} '


ca = float(input('Informe o cateto adjacente.: '))
co = float(input('Informe o cateto oposto.: '))
print(hipotenusa(ca, co))
