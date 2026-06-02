import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.google.com')
except urllib.error.URLError:
    print('\033[31mO site do Google não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site do Google com sucesso!\033[m')
