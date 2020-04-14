from validadores import leiaReal


def convRealDolar(r):
    dolar = r / 5.37
    return '=' * 20 +f'\nValor em R${r:.2f}\nUS${dolar:.2f}\n'+'=' * 20


real = leiaReal('Informe quantos reais possui.: R$')
print(convRealDolar(real))