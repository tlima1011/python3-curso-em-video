def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print( '\033[31mSaída do usuário.\033[m')
            return 0
        else:
            return n



num = leiaInt('Informe um valor inteiro válido.: ')
num1 = leiaFloat('Informe um valor real válido.: ')
print(f'O valor inteiro válido digitado foi {num} e o valor real digitado foi {num1}')
