frase = input('Coloque uma frase embaixo!!!\n')
frase = frase.strip()
frase = frase.lower()
a = input('Informe uma letra para buscar na frase.: ')
a = a.lower()
print(f'Quantidade de {a}: {frase.count(a)}')
print(f'A primeira letra apareceu na posição {frase.find(a)+1}')
print(f'A última letra apareceu na posição {frase.rfind(a)+1}')




