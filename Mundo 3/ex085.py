# Exercício 85. Crie um programa onde o usuário possa digitar sete valores numéricos e cadadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = list()
pares = list()
impares = list()
verifica = list()
for c in range(7):
    verifica.append(int(input(f"Digite o {c+1}º valor: ")))
    if verifica[0] % 2 == 0:
        pares.append(verifica[0])
    else:
        impares.append(verifica[0])
    verifica.clear()

pares.sort()
impares.sort()
lista.append(pares[:])
lista.append(impares[:])

print(f"Pares: {lista[0]}")
print(f"Ímpares: {lista[1]}")

# Solução Professor:

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f"Pares: {num[0]}")
print(f"Ímpares: {num[1]}")