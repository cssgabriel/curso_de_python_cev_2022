# Exercício 90. Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno["Nome"] = str(input("Digite seu nome? "))
aluno["Média"] = float(input("Qual foi a média? "))
print("-=" * 15)

if aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"
elif 5 <= aluno["Média"] < 7:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Reprovado"
for k, v in aluno.items():
    print(f"- {k}: {v}")
