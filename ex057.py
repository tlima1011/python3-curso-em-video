def def_sexo(sexo):
    if sexo == 'M':
        return '\033[1;34mSeu sexo é Masculino\033[m'
    else:
        return '\033[1;91mSeu sexo é Feminino\033[m'


sexo = 'I'
while sexo not in 'MF':
    sexo = str(input('Informe o sexo [M/F]: ').upper().strip())[0]
    if sexo not in 'MF':
        print('\033[1;31mInválido digite novamente!!! Necessário ser [M / F] - Try again\033[m')
print(def_sexo(sexo))

