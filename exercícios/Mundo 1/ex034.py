# Exercício 34. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual seu salário atual? "))
if salario > 1250:
    print("Você ganhou um aumento de 10%. Seu salário agora será de R$ {}".format(salario * 1.10))
else:
    print("Você ganhou um aumento de 15%. Seu salário agora será de R$ {}".format(salario * 1.15))