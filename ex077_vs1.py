palavras = (input('Informe uma palavra: '),
            input('Informe uma outra palavra: '),
            input('Informe mais uma palavra: '))
vogais = ('a', 'à', 'á', 'ã', 'â', 'e', 'é', "ê", 'i', 'í', 'o', 'u', 'ú', 'ü')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in vogais:
            print(letra, end=' ')