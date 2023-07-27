# Exercício 67. Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input("Qual tabuada você quer ver? "))
    if n < 0:
        break
    c = 0
    for c in range(0, 10):
        print(f"{n} X {c} = {n * c}")
print("Programa finalizado!")