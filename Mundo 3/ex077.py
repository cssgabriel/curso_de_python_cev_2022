# Exercício 77. Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

lista = (
    "cobra",
    "macaco",
    "baleia",
    "golfinho",
    "galinha",
    "coala",
    "cachorro",
    "gato",
    "cavalo",
    "pato"
)

for c in lista:
    print(f"Na palavra {c.upper()}, temos: ", end="")
    for l in c:
        if l.lower() in "aeiou":
            print(l, end="")
    print("!")