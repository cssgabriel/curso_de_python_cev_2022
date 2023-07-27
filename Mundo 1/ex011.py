# Exercício 11: Faça um programa que leia a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2

altura = float(input("Altura: "))
largura = float(input("Largura: "))
area = altura * largura
tinta = area / 2
print("Sua parede possui {:.3f}m². Para pintar esta área você precisará de {:.3f} litros de tinta".format(area, tinta))
