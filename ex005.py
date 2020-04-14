def antecessorSucessor(n):
    return f'O número anterior de {n} é {n-1}\no número sucessor é {n+1}'


numero = int(input('Digite um número.: '))
print(antecessorSucessor(numero))