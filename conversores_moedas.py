def convRealDolar(r):
    dolar = r / 5.40
    return ('=' * 20 +f'\nValor em R${r:.2f}\nUS${dolar:.2f}\n'+'=' * 20)


def convDolarReal(d):
    r = d * 4.40
    return ('=' * 20 + f'\nValor em US${d:.2f}\nR${r:.2f}\n' + '=' * 20)


def convRealEuro(r):
    dolar = r / 4.75
    return ('=' * 20 +f'\nValor em R${r:.2f}\n€{dolar:.2f}\n'+'=' * 20)


def convEuroReal(e):
    r = e * 4.75
    return ('=' * 20 + '\nValor em €{:.2f}\nR${:.2f}\n' + '=' * 20).format(e, r)