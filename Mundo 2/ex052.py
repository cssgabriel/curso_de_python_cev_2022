# Exercício 52. Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um número: "))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print("Esse número é divisível por: {} ".format(c))
if cont == 2:
    print("Foi dividido apenas {} vezes, por isso ele é um número PRIMO".format(cont))
else:
    print("Esse número foi divido {} vezes. Não é PRIMO".format(cont))
