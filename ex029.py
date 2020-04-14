def multa(km):
    if km > 80:
        multa = (km - 80) * 7
        return '\033[1;31mCom a velocidade de {}km/h, valor da multa R${:.2f}'.format(km, multa)
    else:
        return '\033[1;32mEstá abaixo de {:.2f}km/h e dirija sempre com segurança!!!\033[m'.format(km)


kmh = float(input('\033[1;34mVelocidade do veículo.: '))
print(multa(kmh))
