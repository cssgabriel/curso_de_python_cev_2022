# Exercício 89. Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = list()
dados = list()
media = soma = 0

while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Nota 1: ")))
    dados.append(float(input("Nota 2: ")))
    soma = dados[1] + dados[2]
    media = soma / 2
    dados.append(media)
    lista.append(dados[:])

    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == "N":
        dados.clear()
        break
    dados.clear()

print("-" * 30)
print(f"{'Nº':<5}", f"{'NOME':<15}", f"{'MÉDIA':<10}")
print("-" * 30)

for i, c in enumerate(lista):
    print(f"{i:<5}", f"{c[0]:<15}", f"{c[3]:<10.1f}")
print("-=" * 15)

while opcao != 999:
    opcao = int(input("Mostrar notas de qual aluno? \33[1;34m[999 interrompe]\33[m "))
    if opcao >= 0 and opcao < len(lista):
        print(f"{lista[opcao][0]} obteve as seguintes notas: {lista[opcao][1:3]}")
    elif opcao != 999:
        print("Valor inválido. Tente novamente!")
    else:
        print("Programa encerrado!")