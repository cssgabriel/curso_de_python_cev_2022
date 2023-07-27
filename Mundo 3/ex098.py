# Exercício 98. Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1.
# B) De 10 até 0, de 2 em 2.
# C) Uma contagem personalizada.

from time import sleep
def contador():
    for c in range(1, 11):
        print(f"{c:2}", end=" ", flush=True)
        sleep(0.5)
    print()

    for c in range(10, 0, -1):
        print(f"{c:2}", end=" ", flush=True)
        sleep(0.5)
    print()

    print(f"="*30)
    print("Personalize agora sua contagem")
    print(f"="*30)
    i = int(input(f"{'Início':<6}{': '}"))
    f = int(input(f"{'Fim':<6}{': '}"))
    p = int(input(f"{'Passo':<6}{': '}"))
    print(f"-="*15)
    if p < 0:
        for c in range(i, f - 1, p):
            print(f"{c:2}", end=" ", flush=True)
            sleep(0.5)
    elif p > 0:
        for c in range(i, f + 1, p):
            print(f"{c:2}", end=" ", flush=True)
            sleep(0.5)
    else:
        p = 1
        for c in range(i, f + 1, p):
            print(f"{c:2}", end=" ", flush=True)
            sleep(0.5)
    print("FIM")


contador()