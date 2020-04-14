def aumento(s):
    if s > 1250:
        novo = s + (s * 0.10)
        return f'\033[1;32mSalário atual R${s:.2f}\nAumento {0.10 * 100}%\nNovo Salário R${novo:.2f}\033[m'
    else:
        novo = s + (s * 0.15)
        return f'\033[1;32mSalário atual R${s:.2f}\nAumento {0.15 * 100}%\nNovo Salário R${novo:.2f}\033[m'