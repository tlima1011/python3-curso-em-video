def total(d, k):
    diaria = 60
    porKm = 0.15
    valorDia = diaria * d
    valorKm = porKm * k
    total = valorDia + valorKm
    return f'Diária R${diaria:.2f}' \
           f'\nValor Km R${porKm:.2f}' \
           f'\nDias alugados: {d}' \
           f'\n{k}km rodados' \
           f'\nTotal a pagar R${total:.2f}'


dias = int(input('Dias alugados.: '))
km = float(input('Quantos km rodados.: '))
print(total(dias, km))
