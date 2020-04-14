from validadores import leiaInt
numeros = []
while True:
    numeros.append(leiaInt('Informe um número.: '))
    continuar = str(input('Quantos valores para continuar {S/N]').strip().upper()[0])
    if continuar == 'N':
        break

numeros.sort(reverse=True)
print(f'Quantidade de números digitados {len(numeros)}')
print(f'Números Ordenados de forma Decrescente: {numeros}')

pesq = str(input('Deseja fazer pesquisa de número da lista {S/N] ').upper().strip()[0])
if pesq in 'sS':
    num_pesquisa = leiaInt('Informe um número para pesquisar: ')
    if num_pesquisa in numeros:
        print(f'O número {num_pesquisa} encontrado na {numeros.index(num_pesquisa)+1}ª posição ')
    else:
        print(f'O número {num_pesquisa} não foi encontrado')
else:
    print('Tenha um bom dia!!!')