import csv


def cadastrar():
    print('-' * 45)
    print(f'{"*** NOVO CADASTRO ***":^45}' )
    print('-' * 45)
    pessoas = dict()
    dados = list()
    nomes = []
    csvFile = open('dados.csv', 'at', newline='')
    csvWriter = csv.writer(csvFile, delimiter=',', lineterminator='\n')
    for e in dados:
        nomes.append(e['nomes'].upper())
    if csvWriter.writerow != 'null':
        novoNome = str(input('Digite novo nome.: '))
        if novoNome.upper() not in nomes:
            pessoas["nomes"] = novoNome
            idade = str(input('Informe a idade.: '))
            while not idade.isnumeric():
                print('Inválido e não será adicionado...')
                idade = str(input( 'Informe a idade.: '))
            pessoas["idade"] = int(idade)
            dados.append(pessoas.copy())
            csvWriter.writerow([novoNome, idade])
            pessoas.clear()
            print(f'O dados de {novoNome} foi cadastrado com sucesso')
        else:
            print('Não será adicionado, pois tem no campo nome não irá funcionar' )


def listar():
    print('-' * 45)
    print(f'{"*** PESSOAS CADASTRADAS ***":^45}')
    print('-' * 45)
    valores = []
    ref_arquivo = open('dados.csv', 'r')
    for linha in ref_arquivo:
        valores = linha.split(',')
        valores[1] = valores[1].replace('\n', '')
        print(f'Nome: {valores[0]:<20} Idade: {valores[1]} anos')
    ref_arquivo.close()


