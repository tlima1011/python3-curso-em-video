from calculadora import somar, subtrair, mutliplicar, dividir
while True:
    numero1 = str(input('Digite um valor.: '))
    numero2 = str(input('Digite outro valor.: '))
    if numero1.isnumeric() and numero2.isnumeric():
        numero1 = int(numero1)
        numero2 = int(numero2)
        print(somar(numero1, numero2))
        print(subtrair(numero1, numero2))
        print(mutliplicar(numero1, numero2))
        print(dividir(numero1, numero2))
    else:
        print(f'Não são números, informe novamente')

    #and numero2 is n
    #print(somar(numero1, numero2))

