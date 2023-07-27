# Exercício 68. Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
cont = 0
while True:
    maquina = randint(1, 10)
    print("-=-" * 13)
    print("Vamos jogar PAR ou ÍMPAR")
    print("-=-" * 13)
    jogador = int(input("Digite um valor: "))
    escolha = str(input("Você quer PAR ou ÍMPAR [P/I]? ")).strip().upper()
    soma = maquina + jogador
    if soma % 2 == 0 and escolha == "P":
        print(f"Você VENCEU! Você jogou {jogador} e o computador jogou {maquina}. A soma é {soma}.\nJogue mais uma vez...")
        cont += 1
    elif soma % 2 != 0 and escolha == "I":
        print(f"Você VENCEU! Você jogou {jogador} e o computador jogou {maquina}. A soma é {soma}.\nJogue mais uma vez...")
        cont += 1
    else:
        print(f"Você PERDEU! Você jogou {jogador} e o computador jogou {maquina}. A soma é {soma}.\nVocê teve {cont} vitórias consecutivas.")
        break