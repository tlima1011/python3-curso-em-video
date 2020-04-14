from statistics import mode, median, mean, variance, stdev
import math
num = (10, 6, 7, 5, 9, 6, 6, 7, 8)
num = sorted(num)
#a)A população é 20
print(f'A amostra - rol crescente -> {num}')
print(f'Quantidade de números: {len(num)}')
print(f'É uma variável continua com números reais')
print(f'A Moda é {mode(num)}') #Função de tiar a moda, qual número
print(f'Mediana é {median(num)}') #Função para tirar mediana
print(f'A Média = {mean(num):.1f}') #Média aritmética
print(f'A Variância: {variance(num):.2f}') #Variância
print(f'Desvio Padrão: {stdev(num):.2f}') #Desvio padrão
cv = (stdev(num) / len(num)) * 100
print(f'Coeficiente de Variação: {cv:.1f}%') #Coeficiente de variação


