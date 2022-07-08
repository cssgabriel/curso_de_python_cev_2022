# Exercício 57. Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Sexo [F/M]: ")).strip().upper()[0]
while sexo not in "MF":
    sexo = str(input("Resposta inválida. Digite novamente! Sexo [F/M]: ")).strip().upper()[0]
print("Ok, agora deu certo!")
