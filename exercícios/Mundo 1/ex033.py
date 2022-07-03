# Exercício 33. Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
maior = n1
# Maior
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
#Menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print("Menor: {}\nMaior: {}".format(menor, maior))
