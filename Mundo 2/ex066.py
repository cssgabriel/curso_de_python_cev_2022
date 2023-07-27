# Exercício 66. Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elels (desconsiderando o flag).

c = 0
soma = 0
while True:
    valor = int(input("Digite um valor [999 para parar]: "))
    if valor == 999:
        break
    c += 1
    soma += valor
print(f"Você digitou {c} valores, e soma entre eles é {soma}")
