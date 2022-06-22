# Exercício 36. Escreva um programa para aprovar o empréstimo bancário para a compra e uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
import time
casa = float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual o seu salário? R$ "))
anos = int(input("Quantos anos para quitar? "))
parcela = casa / (anos * 12)
limite = salario * 30 / 100
print("Para comprar uma cada no valor de R$ {:.2f} em {} anos, o valor da parcela deverá ser R$ {:.2f}.".format(casa, anos, parcela))
print("Calculando seu empréstimo...")
time.sleep(2)
if parcela > limite:
    print("Seu empréstimo foi \33[1;31mNEGADO!\33[m")
else:
    print("Seu empréstimo foi \33[1;32mAPROVADO!\33[m")
