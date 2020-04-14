nome = str(input('Digite algo.: '))
numero = 0.0
numero1 = 0.0
print(nome.isalpha())
print(nome.isdecimal())
#for i in range(0, len(nome)):
#    print(nome[i])
print(nome[-3:])
if ',' in nome[-3:]:
    print('Possui vírgula')
    numero1 = nome[:].replace(',', '.')
else:
    print('Não Possui vírgula')

if '.' in nome[-3:]:
    print('Possui Ponto')
    # return f'{moeda}{preco:.2f}'.replace( '.', '.' )
    numero = float(nome)
else:
    print('Não Possui Não possui ponto')

print(numero)
print(numero1)



