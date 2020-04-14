turma = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'Digite a nota {i} {j}: ')))
    turma.append(linha)

for i in range(3):
    print(turma[i])