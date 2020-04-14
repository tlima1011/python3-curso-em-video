palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro', 'ungüento')
vogais = ('a', 'à', 'á', 'ã', 'â', 'e', 'é', "ê", 'i', 'í', 'o', 'u', 'ú', 'ü')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in vogais:
            print(letra, end=' ')


