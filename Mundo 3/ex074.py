# Exercício 74. Crie um programa cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

sorteio = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print("Eu sorteei os números: ")
for c in sorteio:
    print(f"{c} ", end="")
print(f"\nO maior valor foi {max(sorteio)}")
print(f"O maior valor foi {min(sorteio)}")