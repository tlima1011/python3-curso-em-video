from validadores import leiaInt

numero = leiaInt('Informe o número da tabuada.: ')
inicio = leiaInt('Começa com qual número.: ')
final = leiaInt('Termina com qual número.: ')
print('\033[1;36m=\033[m' * 15 +f'\n\033[1;36mTABUADA DE: {numero}\033[m')
print('\033[1;36m=\033[m' * 15)
for i in range(inicio, final+1):
    print(f'\033[1;33m{numero} x {i} = {numero * i}\033[m')
print('\033[1;36m=\033[m' * 15)