# Exercício 82. Crie um programa que vai ler vários números e colocar em uma lista. Depois crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. A final, mostre o conteúdo das três listas geradas.

lista = list()
pares = list()
impares = list()
cont = 0
while True:
    num = int(input("Digite: "))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == "N":
        cont += 1
        break
    cont += 1

print(f"A lista gerada foi: {lista}")
print(f"Os números pares são: {pares}")
print(f"Os números ímpares são: {impares}")