from validadores import leiaInt
listanum = []
mai = 0
men = 0
count = 0
for c in range(0, 5):
    count += 1
    listanum.append(leiaInt(f'Digite um número para a {count}ª posição: '))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'=-' * 30)
print(f'O maior valor digitado foi {mai} nas posições', end=' ')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {men} nas posições', end=' ')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end=' ')
