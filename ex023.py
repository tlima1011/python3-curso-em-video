numero = int(input('Digite um número.: '))
#print(numero.split())
#print(num)
unidade = numero % 10
dez = numero - 3
dez = dez // 10
dezena = dez % 10
centena = (numero - dezena)//100
milhar = (numero - dezena)//1000
print(f'Unidade {unidade}\nDezena {dezena}\nCentena {centena}\nMilhar {milhar}')
#print('Dezena {}' .format(dezena))
#print('Centena {} ' .format(centena))
#print('Milhares {}' .)



