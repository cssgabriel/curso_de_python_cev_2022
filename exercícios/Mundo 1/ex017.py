# Exercício 17: Faça o programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

# Outra opção: from math import hypot
import math
catad = float(input("Cateto adjacente: "))
catop = float(input("Cateto Oposto: "))
hip = math.hypot(catop, catad)
print("A hipotenusa vale {:.3f}!".format(hip))