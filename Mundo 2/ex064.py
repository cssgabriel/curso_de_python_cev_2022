# Exercício 64. Crie um programa que leia vários números inteiros pelo teclado. O programa só vai para quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a sema entre eles (desconsiderando o flag).

n = int(input("Digite um valor: "))
soma = n
cont = 1
while n != 999:
    n = int(input("Digite um valor: "))
    if n != 999:
        soma += n
        cont += 1
print("Você digitou {} números, e a soma é de {}.".format(cont, soma))
