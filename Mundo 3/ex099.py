# Exercício 99. Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    print("Analisando os valores passados...")
    for c in num:
        print(c, end=" ")
    print(f"Foram informados {len(num)} valores ao todo.")
    for i, c in enumerate(num):
        if i == 0 or c > maior:
            maior = c
    print(f"O maior valor informado foi {maior}.")



maior(5,4,4,5,1,3,9)
maior(6,0)
maior(0)
maior(9,1,2,3,5,4)