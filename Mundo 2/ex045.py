# Exercício 45. Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

lista = ["", "PEDRA", "PAPEL", "TESOURA"]
maquina = randint(1, 3)
opcao = int(input("""Vamos jogar Jokenpô. Você contra a máquina! Escolha uma opção: 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Qual sua escolha? """))
sleep(0.5)
print("JO...")
sleep(0.5)
print("KEN...")
sleep(0.5)
print("PÔ!!!")
sleep(0.5)
print("-=-" * 20)
if opcao == maquina:
    print("Você escoleu {}, e a maquina escolheu {}".format(lista[opcao], lista[maquina]))
    print("EMPATE!")
elif opcao == 1 and maquina == 2:
    print("Você escoleu {}, e a maquina escolheu {}".format(lista[opcao], lista[maquina]))
    print("Você PERDEU!")
elif opcao == 2 and maquina == 1:
    print("Você escoleu {}, e a maquina escolheu {}".format(lista[opcao], lista[maquina]))
    print("Você GANHOU!")
elif opcao == 1 and maquina == 3:
    print("Você escoleu {}, e a maquina escolheu {}".format(lista[opcao], lista[maquina]))
    print("Você GANHOU!")
elif opcao == 3 and maquina == 1:
    print("Você escoleu {}, e a maquina escolheu {}".format(lista[opcao], lista[maquina]))
    print("Você PERDEU!")
elif opcao == 2 and maquina == 3:
    print("Você escoleu {}, e a maquina escolheu {}".format(lista[opcao], lista[maquina]))
    print("Você PERDEU!")
elif opcao == 3 and maquina == 2:
    print("Você escoleu {}, e a maquina escolheu {}".format(lista[opcao], lista[maquina]))
    print("Você GANHOU!")
print("-=-" * 20)

