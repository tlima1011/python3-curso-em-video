from validadores import leiaReal
print('-=' * 30)
print(f'{"***ORGANIZAÇÕES TABAJARA***":^30}')
print('-=' * 30)
menor = preco = soma = dinheiro = troco = 0.0
produto = '1'
continuar = 'S'
i = cont = 0
nome_produto_barato = ''
while continuar in 'Ss':
    i += 1
    produto = input(f'Nome do {i}º produto: ').strip()
    preco = leiaReal(f'Valor {i}º do produto R$')
    if i == 1 or preco < menor:
        menor = preco
        nome_produto_barato = produto
    if preco > 1000:
        cont += 1
    soma += preco
    continuar = str(input('Deseja continuar a compra ? [S/N]'))

print(f'Valor total da Compra R$ {soma:.2f}\nProduto mais Barato: {nome_produto_barato} no valor de R${menor:.2f}')
print(f'Produto com valores maior que R$1000,00: {cont}')
print('-=' * 30)
print(f'{"***ORGANIZAÇÕES TABAJARA***":^30}')
print('-=' * 30)
#dinheiro = float(input('Quanto possui de dinheiro R$'))
while soma > dinheiro:
    dinheiro = leiaReal('Quanto possui de dinheiro R$')
    if dinheiro >= soma:
        troco = dinheiro - soma
        print('-' * 30)
        print('***Nota Fiscal Paulista***')
        print(f'Dinheiro R${dinheiro:.2f}')
        print(f'Valor a pagar R${soma:.2f}')
        print(f'Troco R${troco:.2f}')
        print('-' * 30)
        break
    else:
        print('Informe mais dinheiro, senão não sai da Loja e vem a polícia')
print('Volte mais vezes!!!')




