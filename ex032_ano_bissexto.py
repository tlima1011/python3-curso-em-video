def ano_bissexto(a):
    from datetime import date
    if a == 0:
        a = date.today().year
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        return f'O ano de {a} é bissexto'
    else:
        return f'O ano de {a} não é bissexto'