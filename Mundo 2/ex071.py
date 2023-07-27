# Exercício 71. Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# obs: considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10, e R$1

print("=" * 20)
print("{:^20}".format("BANCO CSS"))
print("=" * 20)
c50 = c20 = c10 = c1 = total = 0
while True:
    saque = float(input("Que valor você quer sacar? R$ "))
    while saque > 50:
        c50 += 1
        saque -= 50
    while saque > 20:
        c20 += 1
        saque -= 20
    while saque > 10:
        c10 += 1
        saque -= 10
    while saque > 0:
        c1 += 1
        saque -= 1
    total = c50 + c20 + c10 + c1
    break
print(f"Foram utilizadas {total} cédulas. Sendo elas: ")
print(f"{c50} cédulas de R$ 50")
print(f"{c20} cédulas de R$ 20")
print(f"{c10} cédulas de R$ 10")
print(f"{c1} cédulas de R$ 1")

