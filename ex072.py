from validadores import leiaInt
nums_extenso = ('zero'.title(), 'um'.title(), 'dois'.title(), 'tres'.title(),
                'quatro'.title(), 'cinco'.title(), 'seis'.title(), 'sete'.title(),'oito'.title(),
                'nove'.title(), 'dez'.title(), 'onze'.title(), 'doze'.title(),
                'treze'.title(), 'catorze'.title(), 'quinze'.title(),
                'dezesseis'.title(), 'dezessete'.title(), 'dezoito'.title(), 'dezenove'.title(), 'vinte'.title())
numero = -9
while numero < 0 or numero > 20:
    numero = leiaInt('Digite um número entre 0 e 20: ')
    if numero < 0 or numero > 20:
        print('Inválido Novamente...Digite novamente')
    else:
        for i in range(0, len(nums_extenso)):
            if nums_extenso[i] == nums_extenso[numero]:
                print(f'Você digitou o número {nums_extenso[numero]}')
print('FIM')




