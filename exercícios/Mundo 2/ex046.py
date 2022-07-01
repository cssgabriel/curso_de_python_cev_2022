# Exercício 46. Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for c in range(10, -1, -1):
    print("{}".format(c))
    sleep(0.5)
print("\33[1;34mBOOM!! BOOM!! POWW!!\33[m")