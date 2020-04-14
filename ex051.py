from validadores import leiaInt
from ex051_pa_pacote import pa


print('\033[1;36m=' * 30 + f'\n{"CALCULO DE PA":^30}\033[m')
print('\033[1;36m=\033[m' * 30)
primeiro_termo = leiaInt('Primeiro termo.: ')
razao = leiaInt('Razão.: ')
print(pa(primeiro_termo, razao))


