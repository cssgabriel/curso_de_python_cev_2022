# Exercício 93. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
jogador["Nome"] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
total = 0
for c in range(partidas):
    gols.append(int(input(f"Quantos gols na partida {c + 1}: ")))
    total += gols[c]
jogador["Gols"] = gols[:]
jogador["Total"] = total
print("-=" * 15)
print(jogador)
print("-=" * 15)
for k, v in jogador.items():
    print(f"O campo {k} tem valor: {v}")
print("-=" * 15)
print(f"O jogador {jogador['Nome']} jogou {partidas} partidas.")
for c, i in enumerate(gols):
    print(f">>> Na partida {c + 1}, fez {i} gols")
print(f"Foi um total de {jogador['Total']} gols")
