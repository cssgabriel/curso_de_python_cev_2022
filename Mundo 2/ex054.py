# Exercício 54. Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

data = date.today().year
maior = 0
menor = 0
for c in range(0,7):
    nasc = int(input("Data de nascimento: "))
    if data - nasc >= 21:
        maior += 1
    else:
        menor += 1
print("{} são maiores.\n{} são menores.".format(maior, menor))