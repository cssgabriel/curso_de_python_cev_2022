# Exercício 106. Fala um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Obs: use cores.
from time import sleep
c = ("\033[m",       # 0 - SEM CORES
    "\033[0;30;41m", # 1 - VERMELHO
    "\033[0;30;42m", # 2 - VERDE
    "\033[0;30;43m", # 3 - AMARELO
    "\033[0;30;44m", # 4 - AZUL
    "\033[0;30;45m", # 5 - ROXO
    "\033[7;30m"     # 6 - BRANCO
)

def ajuda(com):
    titulo("Acessando o manual do comando", 4)
    print(c[6], end="")
    help(com)
    print(c[0])
    sleep(1)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end="")
    print("~" * tam)
    print(f"  {msg}  ")
    print("~" * tam)
    print(c[0])
    sleep(1)


comando = ""
while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO", 1)