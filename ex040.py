from ex040_avaliacao import avaliacao
from validadores import leiaReal


nota1 = leiaReal('Informe a nota 1.: ')
nota2 = leiaReal('Informe a nota 2.: ')
print(avaliacao(nota1, nota2))
