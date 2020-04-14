def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param notas: Uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    numeros = {}
    media = 0.0
    c = total = maior = menor = 0
    for i in range(0, len(notas)):
        if i == 0:
            menor = maior = notas[i]
        else:
            if notas[i] > maior:
                maior = notas[i]
            if notas[i] < menor:
                menor = notas[i]
        total += notas[i]
    media = total / len(notas)
    numeros['total'] = len(notas)
    numeros['media'] = media
    numeros['maior'] = maior
    numeros['menor'] = menor
    if sit == False:
        return numeros
    else:
        if numeros['media'] < 5:
            numeros['situacao'] = 'Ruim'
        elif numeros['media'] < 7:
            numeros['situacao'] = 'Razoável'
        else:
            numeros['situacao'] = 'Boa'
        return numeros


resp = notas(9, 9.7, 6, 8.5, 8, 7, sit=True)
print(resp)
#help(notas)