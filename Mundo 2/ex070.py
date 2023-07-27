# Exercício 70. Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:

# A) qual é o total gasto na compra
# B) Quantos produtos custam mais de R$ 1000.
# C) Qual é o nome do produto mais barato.

total = maior = menor = 0
barato = " "
cont = 0
while True:
    nome = str(input("Nome do produto: "))
    preco = float(input("Preço: R$ "))
    total += preco
    if preco > 1000:
        maior += 1
    if cont == 0 or preco < menor:
        menor = preco
        barato = nome
    opcao = " "
    cont += 1
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == "N":
        break

print("{:-^30}".format("RESUMO DO SEU CARRINHO"))
print(f"O total gasto foi de R$ {total}.")
print(f"{maior} produtos custam mais que R$ 1000.")
print(f"{barato} custa {menor}, e é o produto mais barato.")
print("{:-^30}".format("FIM DO PROGRAMA"))
