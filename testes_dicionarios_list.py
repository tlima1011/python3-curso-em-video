from validadores import leiaInt
import csv
pessoas = dict()
dados = list()
nomes = []
csvFile = open('dados_new.csv', 'at', newline='')
csvWriter = csv.writer(csvFile, delimiter=',', lineterminator='\n')
#dados = [{'nomes': 'Thiago', 'idade': 40}, {'nomes': 'Joao', 'idade': '25'}, {'nomes': 'Maria', 'idade': 25}]
#print(dados)

for e in dados:
    nomes.append(e['nomes'].upper())

novoNome = str(input('Digite novo nome.: '))
pessoas["nomes"] = novoNome
idade = leiaInt('Informe a idade.: ')
pessoas["idade"] = int(idade)
dados.append(pessoas.copy())
pessoas.clear()
csvWriter.writerow([novoNome, idade])
print(dados)

for d in dados:
    print(f'Dados.: {d}')

