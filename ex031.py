from ex031_distancia import distancia
from validadores import leiaReal


kmh = leiaReal('\033[4;36mInforme a distância.: \033[m')
print(distancia(kmh))