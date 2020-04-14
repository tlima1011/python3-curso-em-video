nomeCompleto = str(input('Informe seu nome completo.: ')).strip()
nomeCompleto = nomeCompleto.split()
print(f'Primeiro nome é {nomeCompleto[0].capitalize()} e o último é {nomeCompleto[-1].capitalize()}')
