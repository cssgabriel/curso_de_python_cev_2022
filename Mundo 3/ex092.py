# Exercício 92. Crie um programa que leia nome, ano de nascimento e carteira de trabalho.
# E cadastre-os (com idade) em um dicionário, caso a CTPS for diferente de ZERO.
# O dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
trabalhador = dict()
trabalhador["Nome"] = str(input("Digite seu nome: "))
nascimento = int(input("Digite o ano nascimento: "))
trabalhador["Idade"] = date.today().year - nascimento
trabalhador["CTPS"] = int(input("Carteira de trabalho: [0 - Não Tem] "))
if trabalhador["CTPS"] != 0:
    trabalhador["Contratação"] = int(input("Ano de contratação: "))
    trabalhador["Salário"] = float(input("Salário: R$ "))
    trabalhador["Aposentadoria"] = trabalhador["Idade"] + ((trabalhador["Contratação"] + 35) - date.today().year)
print("-=" * 15)
for k, v in trabalhador.items():
    print(f">>> {k} tem o valor: {v}")
