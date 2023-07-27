# Exercício 42. Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

from time import sleep

reta1 = float(input("Reta 1: "))
reta2 = float(input("Reta 2: "))
reta3 = float(input("Reta 3: "))
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print("Com essas três retas, é possível formar um triângulo")
    print("|  Verificando triângulo...  |")
    sleep(2)
    if reta1 == reta2 and reta3 == reta1:
        print("Todos os lados são iguais. Este é um triângulo EQUILÁTERO!")
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print("Dois lados são iguais. Este é um triângulo ISÓSCELES!")
    else:
        print("Todos os lados são diferentes. Este é um triângulo ESCALENO!")
else:
    print("Com essas três retas, não é possível formar um triângulo.")

