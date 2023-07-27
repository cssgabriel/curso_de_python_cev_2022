# Exercício 75. Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input("Digite um número: ")),
int(input("Digite um número: ")),
int(input("Digite um número: ")),
int(input("Digite um número: ")),)
print(f"Você digitou os valores {num}")
print(f"Os número 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O número 3 apareceu na {num.index(3) + 1}ª posição")
else:
    print("O número 3 não foi digitado")
print(f"Os valores pares foram: ", end="")
for c in num:
    if c % 2 == 0:
        print(f"{c} -> ", end="")
print('fim')