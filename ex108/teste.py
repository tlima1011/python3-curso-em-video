from ex108 import moeda

preco = float(input('Informe o preço em R$'))
aum = float(input('Informe o % de aumento.: '))
dim = float(input('Informe o % para diminuir.: '))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'Aumentando {aum}% temos {moeda.moeda(moeda.aumentar(preco, aum))}')
print(f"Diminuindo {dim}% temos {moeda.moeda(moeda.diminuir(preco, dim))}")