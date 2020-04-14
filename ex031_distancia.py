def distancia(km):
    if km <= 200:
        preco = 0.50
        passagem = km * preco
        return f'\033[4;35mDistângia {km}km - Preço da passagem R${passagem:.2f}\033[m'
    else:
        preco = 0.45
        passagem = km * preco
        return f'\033[4;32mDistângia {km}km - Preço da passagem R${passagem:.2f}\033[m'