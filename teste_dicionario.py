pessoas = dict()
new = list()
for i in range(0, 3):
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoas['nome'] = nome
    pessoas['peso'] = peso
    new.append(pessoas.copy())
    pessoas.clear()
print(new)
for k, v in enumerate(new):
    print(f'Nome: {v["nome"]} - Peso: {v["peso"]}kg')