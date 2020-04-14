nums_extenso = ('zero'.title(), 'um'.title(), 'dois'.title(), 'tres'.title(),
                'quatro'.title(), 'cinco'.title(), 'seis'.title(), 'sete'.title(),'oito'.title(),
                'nove'.title(), 'dez'.title(), 'onze'.title(), 'doze'.title(),
                'treze'.title(), 'catorze'.title(), 'quinze'.title(),
                'dezesseis'.title(), 'dezessete'.title(), 'dezoito'.title(), 'dezenove'.title(), 'vinte'.title())
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente ',end=' ')
print(f'Você digitou o número {nums_extenso[num]}')