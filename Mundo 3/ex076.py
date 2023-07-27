# Exercício 76. Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ("Lápis", 2.50,
"Borracha", 1.00,
"Caderno", 19.90,
"Folha sulfite", 12.00,
"Apontador", 0.50,
"Caixa com clipes", 1.20,
"Régua", 0.70,
"Estojo", 9.50)

print("-" * 40)
print(f"{'Listagem de Preços':^40}")
print("-" * 40)
for c in range(len(listagem)):
    if c % 2 == 0:
        print(f"{listagem[c]:.<30}", end="")
    else:
        print(f"R$ {listagem[c]:>6.2f}")
print("-" * 40)