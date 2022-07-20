# Exercício 14: Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

temperatura = float(input("Qual temperatura em ºC você quer converter para ºF? "))
conversao = (temperatura * 9 / 5) + 32
print("A temperatura de {}ºC corresponde a {}ºF".format(temperatura, conversao))
