# Exercício 22 : Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiúsculas
# -> O nome com todas as letras minúsculas
# -> Quantas letras ao todo (sem considerar espaços)
# -> Quantas letras tem o primeiro nome

nome = str(input("Digite seu nome completo: "))
print("Seu nome em letras maiúsculas: {}".format(nome.upper()))
print("Seu nome em letras minúsculas: {}".format(nome.lower()))
print("Seu nome possui {} letras.".format(len(nome.replace(" ", ""))))
index = nome.split()
print("Seu primeiro nome é {} e possui {} letras.".format(index[0], len(index[0])))