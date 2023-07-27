# Exercício 43. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - Entre 25 e 30: Sobrepeso
# - Entre 30 e 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input("Digite seu peso: Kg "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / altura ** 2
if imc < 18.5:
    print("Seu IMC é de {:.2f}. Você está ABAIXO DO PESO.".format(imc))
elif imc < 25:
    print("Seu IMC é de {:.2f}. Você está com PESO IDEAL.".format(imc))
elif imc < 30:
    print("Seu IMC é de {:.2f}. Você está com SOBREPESO.".format(imc))
elif imc < 40:
    print("Seu IMC é de {:.2f}. Você está OBESO.".format(imc))
else:
    print("Seu IMC é de {:.2f}. Você está com OBESIDADE MÓBIDA.".format(imc))

