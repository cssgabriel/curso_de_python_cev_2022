# Exercício 111. Crie um paco chamado utilidadescev que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos dasafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidades import moeda

preco = float(input("Digite um valor: "))
moeda.resumo(preco, 15, 15)
