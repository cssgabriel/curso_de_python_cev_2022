# Exercício 28. Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
# Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente advinhar...")
print("-=-" * 20)
n = int(input("Em qual número estou pensando? "))
print("PENSANDO...")
sleep(2)
maquina = randint(0, 5)
if n == maquina:
    print("Parabéns, você acertou!")
else:
    print("Não foi dessa vez. Pensei no número {}!".format(maquina))
print("Jogo encerrado.")
