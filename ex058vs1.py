from random import randint
from time import sleep
vezes = 0
num_cpu1 = 1
num_cpu = 0
print('\033[1;32m-=-\033[m' * 40)
while num_cpu1 != num_cpu:
    num_cpu1 = randint(0, 10)
    num_cpu = randint(0, 10)
    print('\033[1;32mProcessando...\033[m')
    sleep(1)
    if num_cpu != num_cpu1:
        print(f'\033[1;31mA CPU1 perdeu /// CPU: [{num_cpu}] - CPU1 [{num_cpu1}]///\033[m')
        vezes += 1
print(f'\033[1;32mA CPU1 acertou o Placar ///CPU: [{num_cpu}] - CPU1 [{num_cpu1}]///\033[m')
print(f'Foram neceessário {vezes} vezes para Acertar')
