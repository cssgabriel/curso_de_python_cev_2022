# Exercício 59. Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
# Seu programa deverá realizar a operação solicitada em cada caso.
# [1] somar
# [2] multiplicar
# [3] mostrar maior
# [4] novos números
# [5] sair do programa

from time import sleep

opcao = 0
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
while opcao != 5:
    print("-=" * 10)
    print("Qual opção você deseja?")
    print("-" * 20)
    print("""
    [1] somar
    [2] multiplicar
    [3] mostrar maior
    [4] novos números
    [5] sair do programa
    """)
    print("-" * 20)
    opcao = int(input("Digite sua escolha: "))
    if opcao == 1:
        soma = n1 + n2
        print("\33[1;34mO resultado da soma entre {} e {} é {}.\33[m".format(n1, n2, soma))
        print("Deseja realizar mais alguma operação? Escolha uma das opções abaixo.")
        sleep(1)
    elif opcao == 2:
        mult = n1 * n2
        print("\33[1;34mO resultado da multiplicação entre {} e {} é {}.\33[m".format(n1, n2, mult))
        print("Deseja realizar mais alguma operação? Escolha uma das opções abaixo.")
        sleep(1)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print("\33[1;34mEntre os números {} e {} o maior é {}.\33[m".format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print("\33[1;34mEntre os números {} e {} o maior é {}.\33[m".format(n1, n2, maior))
        else:
            print("\33[1;34mNão há maior! Os valores são iguais.\33[m")
        print("Deseja realizar mais alguma operação? Escolha uma das opções abaixo.")
        sleep(1)
    elif opcao == 4:
        n1 = int(input("Primeiro número: "))
        n2 = int(input("Segundo número: "))
        soma = 0
        mult = 0
        maior = 0
    elif opcao == 5:
        print("\33[1;34mEncerrando aplicação...\33[m")
        sleep(1)
    else:
        print("\33[1;34mOpção inválida! Digite um número entre 1 e 5.\33[m")
        sleep(1)
