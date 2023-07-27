# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

variavel = input("Digite algo: ")
print("O tipo primitivo desse valor é:", type(variavel))
print("É um número?", variavel.isnumeric())
print("É alfabético?", variavel.isalpha())
print("É alphanumérico?", variavel.isalnum())
print("Possui apenas espaços?", variavel.isspace())
print("Está em maiúsculo?", variavel.isupper())
print("Está em minúsculo?", variavel.islower())
print("Está capitalizada?", variavel.istitle())

