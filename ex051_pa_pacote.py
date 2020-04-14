def pa(pt, r):
    soma = 0
    for i in range(0, 10):
        print(pt, end=' => ')
        pt += r
        soma += pt
    print('TÉRMINO DE DEZ TERMOS')
    termos = '\nA soma dos termos: {}\nA Média: {:.1f}'.format(soma, soma / 10)
    return termos