def avaliacao(n1,n2):
    m = (n1 + n2) / 2
    print('\033[4;34m...:::BOLETIM ESCOLAR PIKAS:::...\033[m')
    if m >= 7:
        return f'\033[1;34mNOTA1: {n1:.1f}\nNOTA2: {n2:.1f}\033[m\n\033[1;32mMÉDIA: {m:.1f}\033[m\nCondição = \033[1;32mAPROVADO\033[m'
    elif 5 <= m < 7:
        return f'\033[1;34mNOTA1: {n1:.1f}\nNOTA2: {n2:.1f}\033[m\n\033[1;33mMÉDIA: {m:.1f}\033[m\nCondição = \033[1;33mRECUPERAÇAO\033[m'
    else:
        return f'\033[1;34mNOTA1: {n1:.1f}\nNOTA2: {n2:.1f}\033[m\n\033[1;31mMÉDIA: {m:.1f}\033[m\nCondição = \033[1;31mREPROVADO\033[m'