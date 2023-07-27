# Exercício 95. Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
gols = list()
time = list()
while True:
    gols.clear()
    jogador.clear()
    jogador["Nome"] = str(input("Nome do jogador: "))
    partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
    total = 0
    for c in range(partidas):
        gols.append(int(input(f"Quantos gols na partida {c + 1}: ")))
        total += gols[c]
    jogador["Gols"] = gols[:]
    jogador["Total"] = total
    jogador["Partidas"] = partidas
    time.append(jogador.copy())

    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if opcao not in "SN":
            print("Opção invalálida. Digite apenas S ou N.")
    if opcao == "N":
        break

print("-" * 50)
print(f"{'Cod':<4}", f"{'NOME':<8}", f"{'GOLS':<25}", f"{'TOTAL':<4}")
print("-" * 50)

for k, v in enumerate(time):
    print(f"{k:<4}", end=" ")
    for d in v.keys():
        if d == "Nome":
            print(f"{v['Nome']:<8}", end=" ")
        elif d == "Gols":
            print(f"{str(v['Gols']):<25}", end=" ")
        elif d == "Total":
            print(f"{v['Total']:<4}", end=" ")
    print()

print("-=" * 25)
while True:
    opcao = 0
    while opcao != 999 or opcao >= len(time):
        opcao = int(input("Mostrar dados de qual jogador? (999 interrompe) "))
        if opcao < len(time) and opcao >= 0 or opcao == 999:
            break
        else:
            print(f"Opção inválida. Digite um número entre 0 e {len(time) - 1}. ")
    if opcao == 999:
        break
    else:
        print(f"Levantamento do jogador -> \33[1;35m{time[opcao]['Nome']}\33[m!")
        print("-=" * 25)
        print(f"O jogador {time[opcao]['Nome']} jogou {time[opcao]['Partidas']} partidas.")
        for i, g in enumerate(time[opcao]["Gols"]):
            print(f">>> No jogo {i + 1}, fez {g} gols")
        print(f">>> Total de {time[opcao]['Total']} gols!")
print("-=" * 25)
print("<<< VOLTE SEMPRE! >>>")