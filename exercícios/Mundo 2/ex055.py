# Exercício 55. Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0.0
menor = 500.0
for c in range(0,5):
    peso = float(input("Digite o peso: Kg "))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print("O maior peso lido foi de {} Kg. O menor peso lido foi de {} Kg".format(maior, menor))

# Outra forma de solução para atribuição do menor

maior = 0.0
menor = 0.0
for c in range(0,5):
    peso = float(input("Digite o peso: Kg "))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {} Kg. O menor peso lido foi de {} Kg".format(maior, menor))