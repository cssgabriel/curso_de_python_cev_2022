# Exercício 38. Escreva um programa que leia dois númersos inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais.

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
if n2 > n1:
    print("O segundo valor é maior")
elif n1 == n2:
    print("Não existe valor maior, os dois são iguais.")
else:
    print("O primeiro valor é maior")