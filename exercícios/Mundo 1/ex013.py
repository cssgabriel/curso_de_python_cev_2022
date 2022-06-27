# Exercício 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual seu salário? R$"))
aumento = 15
novoSalario = salario + (salario * aumento / 100)
print("Parabéns, com o aumento de {}% , voce passará a ganhar {:.2f}".format(aumento, novoSalario))
