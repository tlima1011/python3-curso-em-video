from validadores import leiaInt
print('=' * 40)
print(f'{"DIGITAÇÃO DE NÚMEROS PIKAS VS1.0":^30}')
print('=' * 40)
numero = soma = tot_par = tot_impar = 0
nums = []
while numero != 999:
    numero = leiaInt('Informe um número\nDigite [\033[1;31m999\033[m]\nCaso queira sair: ')
    nums.append(numero)
    if numero != 999:
        soma += numero
        #cont += 1
        if numero % 2 == 0:
            tot_par += 1
        else:
            tot_impar += 1
    else:
        print('Saindo do programa!!!')

media = soma / len(nums)
print(f'Quantidade de números digitados: {len(nums)}\nSoma de números digitados: {soma}\nMedia {media:.2f}')
print(f'Números Pares: {tot_par}\nNúmeros Ímpares {tot_impar}')

