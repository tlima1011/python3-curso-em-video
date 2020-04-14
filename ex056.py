from validadores import leiaInt, leiaSexo
menos20 = soma = maior = 0
velho = ''

for i in range(1, 5):
    nome = input(f'Nome da {i}ª PESSOA.: ').strip()
    idade = leiaInt('Idade.: ')
    sexo = leiaSexo('Sexo [M/F]: ').strip().upper()
    soma += idade
    if (idade > maior) and (sexo == 'M'):
        velho = nome
        maior = idade
    if (sexo == 'F') and (idade < 20):
        menos20 += 1
print(f'A média das idades é de {soma / 4:.1f} anos')
print(f'A pessoa mais velha é {velho.capitalize()} com {maior} anos')
print(f'Possui {menos20} mulheres com menos de 20 ')
