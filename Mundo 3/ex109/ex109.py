# Exercício 109. Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no desafio 108.

import moeda

preco = float(input("Digite um valor: "))
print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}")
print(f"A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}")
taxa = float(input("Qual a porcentagem? "))
print(f"{moeda.moeda(preco)} mais {taxa}% é {moeda.aumenta(preco, taxa, True)}")
print(f"{moeda.moeda(preco)} menos {taxa}% é {moeda.diminui(preco, taxa, True)}")
