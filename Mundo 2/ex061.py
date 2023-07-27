# Exercício 61. Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))
decimo = termo + (10 - 1) * razao
while termo < decimo + razao:
    if termo < decimo:
        print("{} -> ".format(termo), end="")
    else:
        print("{}".format(termo), end="")
    termo += razao
print("!")

# solução professor

cont = 1
while cont <= 10:
    print("{} -> ".format(termo), end="")
    termo += razao
    cont += 1
print("FIM!")