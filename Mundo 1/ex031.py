# Exercício 31. Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km = float(input("Quantos quilômetros tem a viagem que você pretende fazer? "))
if km <= 200:
    print("O preço da viagem é R${}".format(km * 0.5))
else:
    print("Desconto aplicado. O preço da viagem é R${}".format(km * 0.45))
