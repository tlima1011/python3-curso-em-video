maiores = homens = under20 = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ').upper().strip()[0])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]').upper().strip()[0])
    if idade > 18:
        maiores += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        under20 += 1
    if continuar in 'Nn':
        break
print(f'\nPessoas maiores de 18: {maiores}\nHomens cadastrados: {homens}\nMulheres menos de 20: {under20}')




