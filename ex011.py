def tintas(l, a):
    area = l * a
    litros = area / 2
    return 'Em um parede de {:.2f}m X ' \
           '{:.2f}m e área de {:.2f}m²' \
           ' necessário ter {:.1f} litros de tinta'.format(l, a, area,litros)


largura = (float(input('Quantos metros de largura.: ')))
altura = (float(input('Quantos metros de altura.: ')))
print(tintas(largura, altura))