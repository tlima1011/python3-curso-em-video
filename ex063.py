from ex063_fibonacci_packages import fibo_while, fibo_for

print('-=' * 10)
print(' FIBONACCI VS. 1.0')
print('-=' * 10)
while True:
    n1 = n3 = 0
    n2 = 1
    termos = int(input('Quantos termos: '))
    op = int(input('''[ 1 ] - FIBONACCI COM FOR 
[ 2 ] - FIBONACCI COM WHILE
[ 3 ] - SAIR 
Opção.: '''))
    if op == 1:
        print(fibo_for(n1, n2, n3, termos))
    elif op == 2:
        print(fibo_while(n1, n2, n3, termos))
    elif op == 3:
        print('Saindo do programa')
        break
    else:
        print('Tenve novamente..., opção inváldia')
print('FIM')










