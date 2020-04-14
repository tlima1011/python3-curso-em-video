def ehPrimo(n):
    div = 0
    primo = ''
    for i in range(1, n + 1):
        if (n % i == 0):
            div += 1
        if div == 2:
            primo = 'O número {} é um número primo'.format(n)
        else:
            primo = 'O número {} não é um número primo'.format(n)
    return primo