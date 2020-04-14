from ex061_progressao_pacotes import pa, while_pa
from validadores import leiaInt

print('\033[1;36m=' * 30 + f'\n{"CALCULO DE PA":^30}\033[m')
print('\033[1;36m=\033[m' * 30)
primeiro_termo = leiaInt('Primeiro termo.: ')
razao = leiaInt('Razão.: ')
while True:
    tipoPa = input('''QUAL TIPO DE PA
[ 1 ] - PA COM FOR 
[ 2 ] - PA COM WHILE
[ 3 ] - SAIR
Opção: ''')
    if tipoPa == '1':
        print(pa(primeiro_termo, razao))
    elif tipoPa == '2':
        print(while_pa(primeiro_termo, razao))
    elif tipoPa == '3':
        print('Saindo do Programa...')
        break
    else:
        print('Nada')
print('Bye...')