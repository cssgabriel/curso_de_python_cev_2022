# Exercício 60. Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

from math import factorial
n = int(input("Digite o número: "))
c = n
fat = 1
print("Calculando {}! = ".format(n), end="")
while c > 0:
    print("{}".format(c), end="")
    print(" x " if c > 1 else " = ", end="")
    fat = fat * c
    c -= 1
print(fat)
