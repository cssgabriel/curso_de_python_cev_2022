# Exercício 29. Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input("Qual a velocidade do seu carro? "))
if vel > 80:
    print("Você foi MULTADO!")
    multa = (vel - 80) * 7
    print("Valor da multa: R${:.02f}".format(multa))
else:
    print("Você está dentro do limite de velocidade.")
print("Tenha um boa viagem!")