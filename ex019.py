from random import choice


def escolherAluno(n1, n2, n3, n4):
    lista = [n1, n2, n3, n4]
    escolhido = choice(lista)
    return f'O escolhido foi.: {escolhido}'


nome1 = input('Nome do primeiro aluno: ')
nome2 = input('Nome do segundo aluno: ')
nome3 = input('Nome do terceiro aluno: ')
nome4 = input('Nome do quarto aluno: ')
print(escolherAluno(nome1, nome2, nome3, nome4))