def compra(c, s, a):
    prestacao = c / (a * 12)
    minimo = s * 30 / 100
    print(f'Para pagar uma casa de R${c:.2f} em {a} anos\nA prestação será de R${prestacao:.2f}')
    if prestacao <= minimo:
        return '\033[1;32mEmpréstimo pode ser CONCEDIDO!!!\033[m'
    else:
        return '\033[1;31mEmpréstimo NEGADO!!!\033[m'
