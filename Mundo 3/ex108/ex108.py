import moeda

preco = float(input("Digite um valor: "))
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}")
print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}")
taxa = float(input("Qual a porcentagem? "))
print(f"{moeda.moeda(preco)} mais {taxa}% é {moeda.moeda(moeda.aumenta(preco, taxa))}")
print(f"{moeda.moeda(preco)} menos {taxa}% é {moeda.moeda(moeda.diminui(preco, taxa))}")
