# Exercício 78. Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
menor = maior = 0

for c in range(5):
    lista.append(int(input(f"Digite um valor para adicionar na posição {c}: ")))
    if c == 0:
        menor = lista[c]
        maior = lista[c]
    else:
        if lista[c] < menor:
            menor = lista[c]
        if lista[c] > maior:
            maior = lista[c]

print(f"Os valores são: {lista}")
print(f"O maior valor foi: {maior}. E ele aparece na(s) posição(ões) ", end="")
for c, v in enumerate(lista):
    if v == maior:
        print(f"{c}...", end="")
print(f"\nO menor valor foi: {menor}. E ele aparece na(s) posição(ões) ", end="")
for c, v in enumerate(lista):
    if v == menor:
        print(f"{c}...", end="")



