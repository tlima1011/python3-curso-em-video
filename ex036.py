from validadores import leiaReal, leiaInt
from ex036_compra import compra


casa = leiaReal('Qual o valor da casa R$')
salario = leiaReal('Salário R$')
anos = leiaInt('Anos para pagar.: ')
print(compra(casa, salario, anos))