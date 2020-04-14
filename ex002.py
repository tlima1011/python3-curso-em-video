def prazer(n):
    return f'É um prazer te conhecer, \033[1;32m{n.capitalize()}\033[m!'


nome = input('Digite seu nome.: ')
print(prazer(nome))