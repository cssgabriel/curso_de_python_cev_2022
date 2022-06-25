# Exercício 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valorProduto = float(input("Preço: R$ "))
desconto = 5
valorFinal = valorProduto - (valorProduto * (desconto / 100))
print("Hoje é seu dia de sorte!\nDesconto de {}% aplicado em seu produto. Custava R$ {}, agora você pode levar por apenas R$ {:.2f}".format(desconto, valorProduto, valorFinal))
