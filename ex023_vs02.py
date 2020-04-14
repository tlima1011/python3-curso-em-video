def particionar(n):
    u = n // 1 % 10
    d = n // 10 % 10
    c = n // 100 % 10
    m = n // 1000 % 10
    return f'Analisando o número... {n}\nUnidade: {u}\nCentena {d}\nCentena {c}\nMilhar {m}'


num = int(input('Digite um número.: '))
print(particionar(num))
