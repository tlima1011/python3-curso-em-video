name = input('Digite algo.: ')
print('O tipo primitivo desse valor é.: ', type(name))
print('Só tem espacos ? ', name.isspace())
print('É um número ?', name.isnumeric())
print('É alfabético ? ', name.isalpha())
print('É alfanumérico ?', name.isalnum())
print("Está em maíusculas ? ", name.isupper())
print('Está em minúsculas ? ', name.islower())
print('Está capitalizada ? ', name.istitle())
print('')


