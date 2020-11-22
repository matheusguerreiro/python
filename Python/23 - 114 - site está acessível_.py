# Aula 23 (Tratamento de Erros e Exceções)

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com')
except urllib.error.URLError:
    print('Deu erro!')
else:
    print('Tudo Ok.')
