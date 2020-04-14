def centimetrosMilimetros(m):
    dm = m * 10
    cm = m * 100
    mm = m * 1000
    dam = m / 10
    hm = m / 100
    km = m / 1000
    return f'{m}m equivale a {dm} decimetros {m}m equivale a {cm} centimetros' \
           '\n{m}m equivale a {mm} milimetros ' \
           '\n{dam}dam equivale a {m} m ' \
           '\n{hm}hm equivale a {m} m ' \
           '\n{km}km equivale a {m} m '


metros = float(input('Informe o valor em metros.: '))
print(centimetrosMilimetros(metros))