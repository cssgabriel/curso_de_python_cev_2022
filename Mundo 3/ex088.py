# Exercício 88. Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print("-"*30)
print(f"{'MEGA SENA':^30}")
print("-"*30)
lista = list()
jogos = int(input("Quantos jogos você deseja? "))

for j in range(jogos):
    cont = 0
    while True:
        valor = randint(1, 60)
        if valor not in lista:
            lista.append(valor)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    print(f"Jogo número {j+1}: {lista}")
    lista.clear()
    sleep(1)
