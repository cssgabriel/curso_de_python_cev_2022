# Exercício 53. Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

from dataclasses import replace


frase = str(input("Digite uma frase: ")).strip().upper()
frase = frase.replace(" ","")
tam = len(frase)
inverso = ""

# solução com o FOR
for c in range(tam - 1, -1 , -1):
    inverso += frase[c]
print("O inverso de {} é {}".format(frase, inverso))
if inverso == frase:
    print("Palindromo")
else:
    print("Não é palindromo")

# solução simplificada
if frase == frase[::-1]:
    print("Palindromo")
else:
    print("Não é palindromo")
