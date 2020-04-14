from datetime import date
from validadores import leiaInt
maiores = menores = soma_maiores = soma_menores = 0
for i in range(1, 8):
    nascimento = leiaInt(f'Informe a {i}ª data de nascimento.: ')
    anoHoje = date.today().year
    idade = anoHoje - nascimento
    if idade >= 21:
        maiores += 1
        soma_maiores += idade
    else:
        menores += 1
        soma_menores += idade

print(f'Maiores de Idade: {maiores}\nMenores de Idade: {menores}')
print(f'Média das pessoas maiores de Idade: {soma_maiores / 7:.2f}')
print(f'Média das pessoas maiores de Idade: {soma_menores / 7:.2f}')
