def jogador(nome, gols):
    if nome == '' and gols == '':
        nome = '<desconhecido>'
        gols = 0
        return f'Nome do Jogador {nome} com gols {gols} marcados.'
    elif nome != '' and gols == '':
        gols = 0
        return f'Nome do Jogador {nome} com gols {gols} marcados.'
    elif gols != '' and nome == '':
        nome = '<desconhecido>'
        return f'Nome do Jogador {nome} com gols {gols} marcados.'
    else:
        return f'Nome do Jogador {nome} com gols {gols} marcados.'


nome = str(input('Informe o nome do Jogador: ')).title().strip()
gols = str(input('Informe os gols: ')).title().strip()
print(jogador(nome, gols))