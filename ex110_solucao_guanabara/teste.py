from ex110_solucao_guanabara import moeda

preco = float(input('Informe o preço em R$'))
aum = float(input('Informe o % de aumento.: '))
dim = float(input('Informe o % para diminuir.: '))
moeda.resumo(preco, aum, dim)

#print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
#print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
#print(f'Aumentando {aum}% temos {moeda.aumentar(preco, aum, True)}')
#print(f"Diminuindo {dim}% temos {moeda.diminuir(preco, dim, True)}")