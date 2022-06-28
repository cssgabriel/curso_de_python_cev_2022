# Exercício 23. Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834;
# unidade: 4; dezena: 3; centena: 8; milhar: 1;

from math import trunc
num = int(input("Digite um número: "))

un = trunc(num % 10)
dz = trunc((num % 100 - un) / 10)
ct = trunc((num % 1000 - dz - un) / 100)
ml = trunc((num % 10000 - ct - dz - un) / 1000)

print("unidade: {}".format(un))
print("dezena: {}".format(dz))
print("centena: {}".format(ct))
print("milhar: {}".format(ml))

# Resolução do professor

un = num // 1 % 10
dz = num // 10 % 10
ct = num // 100 % 10
ml = num // 1000 % 1000


