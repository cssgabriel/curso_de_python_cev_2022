# Exercício 81. Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma descrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
cont = 0
while True:
    lista.append(int(input("Digite: ")))
    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == "N":
        cont += 1
        break
    cont += 1

print(f"Foram digitados {cont} números")
lista.sort(reverse=True)
print(f"A lista em ordem descrescente é: {lista}")
if 5 in lista:
    print("O número 5 está na posição: ", end="")
    for c, v in enumerate(lista):
        if v == 5:
            print(f"{c}...", end="")
else:
    print("Nessa lista não contém o número 5.")