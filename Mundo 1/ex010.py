# Exercício 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. US$ = R$ 5.15.

valor = float(input("Quanto de dinheiro você tem na carteira? R$ "))
dolar = valor / 5.15
print("Com R$ {:.2f} você pode comprar US$ {:.2f}".format(valor, dolar))