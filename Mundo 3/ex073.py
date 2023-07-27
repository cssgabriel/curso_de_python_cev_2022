# Exercício 73. Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Os 5 primeiros.
# B) Os 4 últimos colocados.
# C) Times em ordem alfabética.
# D) Em que posição está o time da Cuiabá.

times = (
"Palmeiras","Corinthians","Athletico-PR","Atlético-MG",
"Internacional","Fluminense","Botafogo","Santos","São Paulo",
"Bragantino","Avaí","Atlético-GO","Ceará SC","Flamengo",
"Coritiba","América-MG","Goiás","Cuiabá","Fortaleza","Juventude"
)

print("Os cinco primeiros colocados são: ")
for c in range(0,5):
    print(f"{times[c]} -> ", end="")
print("FIM")
print("Os quatro últimos colocados são: ")
for c in range(len(times)- 1, len(times) - 6, -1):
    print(f"{times[c]} -> ", end="")
print("FIM")
print("A tupla ordenada é :\n", sorted(times))
print("Cuiabá está na {}ª posição.".format(times.index("Cuiabá")+1))