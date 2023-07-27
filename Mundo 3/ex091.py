# Exercício 91. Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
ranking = list()
for c in range(1, 5):
    num = randint(1, 6)
    jogadores[f"Jogador {c}"] = num
for k, v in jogadores.items():
    print(f"O {k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print("-="*15)
for i, v in enumerate(ranking):
    print(f"{i + 1}º lugar: {v[0]} com {v[1]}")
