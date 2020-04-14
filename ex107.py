from validadores import leiaReal
import moeda
n = leiaReal('Digite o preço em R$')
p = leiaReal('Porcentagem de aumento: ')
x = leiaReal('Porcentagem de diminuição: ')
print(f'A metade de {n} é R${moeda.metade(n)}')
print(f'O dobro de {n} é R${moeda.dobro(n)}')
print(f'Aumentando {p} temos {moeda.aumentar(n,p)}')
print(f'Reduzindo {x} temos {moeda.diminuir(n,x)}')
