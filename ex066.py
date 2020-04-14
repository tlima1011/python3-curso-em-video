totPar = totImpar = cont = soma = media = nums = 0
#while True:
while True:
    cont += 1
    n = int(input(f'Informe o {cont} número (ou digite \033[1;31m999\033[m para interromper): '))
    if n == 999:
        break
    else:
        soma += n
        nums += 1
        if n % 2 == 0:
            totPar += 1
        else:
            totImpar += 1
media = soma / nums
print(f'Números digitados: {nums}\nSoma dos Nùmeros: {soma}\nMédia: {media:.2f}')
print(f'Números Pares {totPar}\nNúmeros Impares {totImpar}')