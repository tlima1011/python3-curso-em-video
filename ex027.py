nomeCompleto = str(input('Informe seu nome completo.: ')).strip()
nomeCompleto = nomeCompleto.split()
primeiroNome = nomeCompleto[0]
primeiroNome = primeiroNome.capitalize()
ultimoNome = nomeCompleto[-1]
ultimoNome = ultimoNome.capitalize()
print(f'Primeiro nome é {primeiroNome} e o último é {ultimoNome}')

