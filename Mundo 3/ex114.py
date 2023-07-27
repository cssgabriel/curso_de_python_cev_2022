# Exercício 114. Crie um código em Python que teste se o site Pudim(pudim.com.br) está acessível pelo computador usado.

import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br")
except urllib.error.URLError:
    print("Deu erro")
else:
    print("Tudo Ok")
