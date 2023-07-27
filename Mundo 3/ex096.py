# Exercício 96. Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    area = l * c
    print(f"{area:.2f}m²")


l = float(input("Largura: "))
c = float(input("Comprimento: "))
area(l, c)