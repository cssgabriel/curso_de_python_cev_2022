# Exercício 100. Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista.
# A segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint

numeros = list()
def sorteio(lista):
    print("Sorteando 5 valores: ", end="")
    for i in range(5):
        lista.append(randint(0,10))
        print(lista[i], end=" ")
    print("- FIM")

def somaPar(lista):
    soma = 0
    print("Somando os valores pares de: ", lista, end="")
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f"Somando os valores pares de: {lista} | Temos: {soma}")


sorteio(numeros)
somaPar(numeros)