# Exercício 107. Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

num = float(input("Digite um valor: R$ "))
print(f"O dobro de R$ {num:.2f} é {moeda.dobro(num):.2f}")
print(f"A metade de R$ {num:.2f} é {moeda.metade(num):.2f}")
taxa = float(input("Qual taxa você deseja aplicar? "))
print(f"R$ {num:.2f} mais {taxa:.2f}% vai para R$ {moeda.aumentar(num, taxa):.2f}")
print(f"R$ {num:.2f} menos {taxa:.2f}% vai para R$ {moeda.diminuir(num, taxa):.2f}")
