# Exercício 8: Escreva um programa que leia um valor em metros e o exiba convertido em quilometros, hectometros, decâmetros, decímetros, centímetros e milímetros.

metros = float(input("Digite um valor em metros: "))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print("{:.0f} Metros equivale a: ".format(metros))
print("{} Quilômetros".format(km))
print("{} Hectômetros".format(hm))
print("{} Decâmetros".format(dam))
print("{:.0f} Decímetros".format(dm))
print("{:.0f} Centímetros".format(cm))
print("{:.0f} Milímetros".format(mm))
