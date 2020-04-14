import requests
import urllib
import urllib.request
try:
    response = urllib.request.urlopen('http://www.pudim.com.br/')
    print('\033[1;32mConsegui aessar o site Pudim com sucesso!!!\033[m')
    #print(response.read())
except requests.RequestException:
    print('\033[1;31mNão foi possível acessar o site Pudim\033[m')


