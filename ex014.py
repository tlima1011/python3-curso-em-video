from temperaturas_conversores import convCf, convFc, convCk, convKc, convFk, convKf
print('-' * 37 + '\n...CONVERSOR PIKAS DE TEMPERATURA...\n' + '-' * 37)
print('[ 1 ] - Celsius / Fahrenheit '
      '\n[ 2 ] - Fahrenheit / Celsius'
      '\n[ 3 ] - Celsius / Kelvin '
      '\n[ 4 ] - Kelvin / Celsius'
      '\n[ 5 ] - Kelvin / Fahrenheit'
      '\n[ 6 ] - Fahrenheit / Kelvin \nOpção. : ')
conversao = input()
if conversao == '1':
    celsius = float(input('Graus em Celsius: '))
    print(convCf(celsius))
elif conversao == '2':
    fahrenheit = float(input('Graus em Fahrenheit: '))
    print(convFc(fahrenheit))
elif conversao == '3':
    celsius = float(input('Graus em Celsius: '))
    print(convCk(celsius))
elif conversao == '4':
    kelvin = float(input('Graus em Kelvin: '))
    print(convKc(kelvin))
elif conversao == '5':
    kelvin = float( input( 'Graus em Kelvin: '))
    print(convKf(kelvin))
elif conversao == '6':
    fahrenheit = float(input('Graus em Fahrenheit: '))
    print(convFk(fahrenheit))
else:
    print('Inválido')