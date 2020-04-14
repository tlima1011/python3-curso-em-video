def media(n1, n2):
    media = (n1 + n2) / 2
    return f'A média de {n1} e {n2} = {media}'


nota1 = float(input('Informe a nota1.: '))
nota2 = float(input('Informe a nota2.: '))
print(media(nota1, nota2))
