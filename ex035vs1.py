from ex035_triangulo_formacao import forma_triangulo
from validadores import leiaReal

print('\033[1;33m=' * 25)
print('Analisador de Triângulos')
print('=' * 25)
reta1 = leiaReal('A primeira reta.: ')
reta2 = leiaReal('A segunda reta.: ')
reta3 = leiaReal('A terceira reta.: ')
print('=' * 25 + '\033[m')
print(forma_triangulo(reta1, reta2, reta3))