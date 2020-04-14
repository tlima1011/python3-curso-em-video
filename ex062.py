from validadores import leiaInt
from ex061_progressao_pacotes import while_pa, while_pa_total

print('-=' * 10)
print('GERADOR DE PA VS 3.0')
print('-=' * 10)
termo = leiaInt('Primeiro termo.: ')
razao = leiaInt('Razão da PA.: ')
total = cont = i = soma = 0
#mais = 10
print(while_pa(termo, razao))
"""
while mais != 0:
    total += mais
    while i < total:
        print(termo, end=' => ' )
        termo += razao
        soma += termo
        i += 1
"""

while True:
    print('PAUSA')
    mais = leiaInt('Quantos termos você quer mostrar a mais: ')
    if mais == 0:
        break
    print(while_pa_total(soma, termo, razao, mais))
print('FIM')


