s = 0
contagem = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
        contagem += 1
print(f'A soma dos números ímpares e múltiplos de 3 = {s} que foram contados {contagem} números')