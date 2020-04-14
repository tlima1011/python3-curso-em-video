from validadores import leiaInt


def pa(pt, r):
    soma = 0
    for i in range(0, 10):
        print(pt, end=' => ')
        pt += r
        soma += pt
    print('TÉRMINO DE DEZ TERMOS')
    termos = '\nA soma dos termos: {}\nA Média: {:.1f}'.format(soma, soma / 10)
    return termos


def while_pa(pt, r):
    soma = 0
    i = 0
    while i < 10:
        print(pt, end=' => ' )
        pt += r
        soma += pt
        i += 1
    global t
    t = pt
    global s
    s = soma
    global razao
    razao = r
    print('TÉRMINO DE DEZ TERMOS')
    termos = '\nA soma dos termos: {}\nA Média: {:.1f}'.format(soma, soma / 10)
    return termos


def while_pa_total(s, r, t,mais):
    i = 0
    while i < mais:
            print(t, end=' => ')
            t += razao
            s += t
            i += 1
    print('TÉRMINO DE DEZ TERMOS')
    termo = f'Término dos termos\nA soma dos termos: {s}\nA Média: {s / 10:.1f}'
    return termo



