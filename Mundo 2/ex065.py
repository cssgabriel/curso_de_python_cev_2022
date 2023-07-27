# Exercício 65. Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = 0
n = int(input("Digite um número: "))
opcao = str(input("Quer continuar? [S/N] ")).strip().upper()
c = 1
soma += n
media = soma / c
maior = n
menor = n
while opcao != "N":

    n = int(input("Digite um número: "))
    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()

    # maior/menor
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

    # soma e média
    soma += n
    c += 1
    media = soma / c

print("Foram digitados {:.2f} valores.".format(c))
print("A soma entre todos números digitados é de {:.2f}.".format(soma))
print("A média de todos os valores é de {:.2f}.".format(media))
print("O maior valor digitado foi {:.2f}, e o menor foi {:.2f}.".format(maior, menor))