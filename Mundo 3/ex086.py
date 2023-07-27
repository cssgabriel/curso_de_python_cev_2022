# Exercício 86. Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
valor = 0
for c in range(9):
    valor = int(input("Digite um valor: "))
    if c < 3:
        matriz[0].append(valor)
    elif c < 6:
        matriz[1].append(valor)
    else:
        matriz[2].append(valor)
print(f"[{matriz[0][0]:^3}] [{matriz[0][1]:^3}] [{matriz[0][2]:^3}]")
print(f"[{matriz[1][0]:^3}] [{matriz[1][1]:^3}] [{matriz[1][2]:^3}]")
print(f"[{matriz[2][0]:^3}] [{matriz[2][1]:^3}] [{matriz[2][2]:^3}]")

# SOLUÇÃO PROFESSOR;

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]: "))
print("-=" * 30)
for l in range(0,3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()