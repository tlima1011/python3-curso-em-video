nome_completo = input('Informe o nome completo.: ').strip()
#print(nome_completo)
maiusculo = nome_completo.upper()
minusculo = nome_completo.lower()
cap = nome_completo.capitalize()
titulo = nome_completo.title()
caracteres = len(nome_completo)-nome_completo.count(' ')
divisao = nome_completo.split()
primeiro = divisao[0]
#print(primeiro)
print(f'Analisando o Nome Completo.: {nome_completo}'
      f'\nMaiusculo.: {maiusculo}'
      f'\nMinúsculo.: {minusculo}'
      f'\nCapitalizado.: {cap}'
      f'\nTitularizado.: {titulo}'
      f'\nQtde Caracteres.: {caracteres}'
      f'\nPrimeiro Nome.: {primeiro.title()}, que possuem {len(primeiro)} letras')

