def imc(p, a):
    imc = p / (a ** 2)
    if imc < 18.5:
        return f'Índice de IMC: {imc:.1f} como \033[0;33mABAIXO DE PESO\033[m'
    elif imc < 25:
        return f'Índice de IMC: {imc:.1f} com \033[0;32mPESO IDEAL\nPARABÉNS!!!\033[m'
    elif imc < 30:
        return f'Índice de IMC: {imc:.1f} com \033[0;31mSOBREPESO\nCUIDADO\033[m'
    elif imc < 40:
        return f'Índice de IMC: {imc:.1f} com \033[0;31mOBESIDADE\nCUIDADO\033[m'
    else:
        return f'Índice de IMC: {imc:.1f} com \033[0;31mOBESIDADE MÓRBIDA\nCUIDADO\033[m'