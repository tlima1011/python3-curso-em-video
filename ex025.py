completo = input('Informe o nome completo.: ').strip()
completo = completo.title()
palavras_divididas = completo.split()
print('Seu nome tem Silva? {}' .format('Silva' in palavras_divididas))
