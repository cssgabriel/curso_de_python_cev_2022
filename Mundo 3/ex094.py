# Exercício 94.Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas se cadastraram
# B) A média de idade.
# C) Uma lista com mulheres
# D) Uma lista com idade acima da média

soma = cont = media = 0
dados = list()
pessoas = dict()
while True:
    pessoas.clear()
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "FM":
        sexo = str(input("Sexo: [F/M] ")).strip().upper()[0]
        if sexo not in "FM":
            print("Opção invalálida. Digite apenas F ou M.")

    pessoas["Nome"] = nome
    pessoas["Idade"] = idade
    pessoas["Sexo"] = sexo
    dados.append(pessoas.copy())
    soma += idade
    cont += 1
    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if opcao not in "SN":
            print("Opção invalálida. Digite apenas S ou N.")
    if opcao == "N":
        break

media = soma / cont
print("-=" * 20)
print(f"A) Ao todo temos {cont} pessoas cadastradas.")
print(f"B) A média de idade é de {media:.2f}.")
print("C) As mulheres cadastradas foram: ", end="")
for c in dados:
    if c["Sexo"] == "F":
        print(f"[{c['Nome']}]", end="")
print()
print("D) Pessoas que estão acima da média:")
print("-" * 40)
for c in dados:
    if c["Idade"] > media:
        print(f">>> Nome: {c['Nome']:>7}; Sexo: {c['Sexo']:>3}; Idade: {c['Idade']:>3};")
print("-=" * 20)
