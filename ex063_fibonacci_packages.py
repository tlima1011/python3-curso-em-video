#Sequencia do Fibonacci
def fibo_for(n1, n2, n3, termos):
    print(n1, end=' -> ')
    print(n2, end=' -> ')
    for i in range(n1, termos-2):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=' -> ')
    return 'FIM'


def fibo_while(n1, n2, n3, termos):
    print(n1, end=' -> ' )
    print(n2, end=' -> ' )
    i = 0
    while i < termos-2:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print( n3, end=' -> ' )
        i += 1
    return 'FIM'