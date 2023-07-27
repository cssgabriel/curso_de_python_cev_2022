# Exercício 58. Melhore o DESAFIO 28 onde o computador vai "pensar" em um número ente 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

maquina = randint(1, 10)
jogador = int(input("Qual número eu pensei? "))
tentativas = 0
while jogador != maquina:
    if maquina > jogador:
        jogador = int(input("Mais... Tente outra vez: "))
        tentativas += 1
    if maquina < jogador:
        jogador = int(input("Menos... Tente outra vez: "))
        tentativas += 1
if jogador == maquina:
    tentativas += 1
    print("Parabéns, você acertou! Eu também pensei no número {}. Você precisou de {} tentativas.".format(maquina, tentativas))

