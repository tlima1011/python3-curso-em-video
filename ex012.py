def preco_novo(preco):
    desconto = 0.05
    precoNovo = preco - (preco * desconto)
    return ('=' * 20 +f'\nPreço Atual R${preco:.2f}\n{desconto * 100}% de desconto\nPreço com desconto\nR${precoNovo:.2f}\n'+'=' * 20)


preco = float(input('Qual o preço atual.: '))
print(preco_novo(preco))