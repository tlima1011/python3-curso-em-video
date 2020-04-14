from ex043_analisador_imc import imc
from validadores import leiaReal
peso = leiaReal('Informe o peso em Kg ')
altura = leiaReal('Informe a altura: ')
print(imc(peso, altura))


