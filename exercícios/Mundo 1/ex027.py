# Exercício 27. Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Exercício: Ana Maria de Souza
# Primeiro: Ana
# Últim: Souza

nome = str(input("Digite seu nome: ")).strip()
separa = nome.split()
print("Seu primeiro nome é {}".format(separa[0]))
print("Seu último nome é {}".format(separa[len(separa) - 1]))
