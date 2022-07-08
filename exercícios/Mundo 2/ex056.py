# Exercício 56. Desenvolva um programa que leia o nome, idade e o sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

maior = 0
media = 0
maisVelho = ""
somaIdade = 0
cont = 0
for c in range(1, 5):
    print("----- {}º PESSOA -----".format(c))
    nome = str(input("Nome: ")).strip().upper()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[F/M]: ")).strip().upper()

    # media
    somaIdade += idade
    media = somaIdade / 4

    # homem mais velho
    if maior < idade and sexo == "M":
        maior = idade
        maisVelho = nome

    # até 20 anos
    if idade <= 20 and sexo == "F":
        cont += 1

print("=" * 15)
print("A média de idade do grupo é de {} anos.".format(media))
print("O nome do homem mais velho é {}.".format(maisVelho))
print("Desse grupo, {} mulheres possuem até 20 anos de idade.".format(cont))
print("=" * 15)
