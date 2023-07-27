# Exercício 69. Crie uma programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

homem = maior = mulher = 0
while True:
    print("-" * 15)
    print("Cadastre uma pessoa")
    print("=-" * 15)
    idade = int(input("Idade: "))
    sexo = ""
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    print("=-" * 15)
    if idade > 18:
        maior += 1
    if sexo == "F" and idade < 20:
        mulher += 1
    if sexo == "M":
        homem += 1

    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar [S/N]?: ")).strip().upper()[0]
    if opcao == "N":
        break

print(f"{maior} pessoas tem mais de 18 anos.")
print(f"{homem} homens foram cadastrados.")
print(f"{mulher} mulheres tem menos de 20 anos.")