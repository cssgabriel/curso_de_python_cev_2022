# Exercício 84. Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = list()
dados = list()
cont = 0
while True:
    dados.append(str(input("Nome: ")).strip())
    dados.append(float(input("Peso: ")))
    lista.append(dados[:])
    dados.clear()
    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == "N":
        cont += 1
        break
    cont += 1

print(f"Foram cadastradas {cont} pessoas.")
# MAIOR PESO
nome = ""
for c, p in enumerate(lista):
    if c == 0 or lista[c][1] > maior:
        maior = lista[c][1]
print(f"O MAIOR peso registrado foi de {maior}Kg. Peso de ", end="")
for c, p in enumerate(lista):
    if lista[c][1] == maior:
        nome = lista[c][0]
        print(f"{nome}...", end="")
print("!")
# MENOR PESO
for c, p in enumerate(lista):
    if c == 0 or lista[c][1] < maior:
        menor = lista[c][1]
print(f"O MENOR peso registrado foi de {menor}Kg. Peso de ", end="")
for c, p in enumerate(lista):
    if lista[c][1] == menor:
        nome = lista[c][0]
        print(f"{nome}...", end="")
print("!")