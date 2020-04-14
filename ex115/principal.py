from ex115 import cores
from ex115 import modulos
while True:
    print('-' * 45)
    print(f'{"*** MENU PRINCIPAL ***":^45}')
    print('-' * 45)
    print(f'\033[1;33m [ 1 ]\033[m  -  \033[1;34mVer Pessoas Cadastradas\033[m')
    print(f'\033[1;33m [ 2 ]\033[m  -  \033[1;34mCadastrar Nova Pessoa\033[m')
    print(f'\033[1;33m [ 3 ]\033[m  -  \033[1;34mSair do Programa\033[m')
    print('-' * 45)
    opcao = str(input('\033[1;33mSua Opção.: \033[m')).strip()
    if opcao == '1':
        modulos.listar()
    elif opcao == '2':
        modulos.cadastrar()
    elif opcao == '3':
        break
    elif opcao == '' or opcao.isalpha():
        print('\033[1;31mERRO!! - Opção Inválida!\033[m')

print('\033[1;31m-\033[m' * 45)
print(f'\033[1;31m{"ATÉ LOGO":^45}\033[m')
print('\033[1;31m-\033[m' * 45)







