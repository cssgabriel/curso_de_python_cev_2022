# Exercício 97. Faça um programa que tneha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    tamanho = len(msg) + 4
    print("~" * tamanho)
    print(f"  {msg}")
    print("~" * tamanho)


msg = str(input("Escreva uma mensagem: "))
escreva(msg)
