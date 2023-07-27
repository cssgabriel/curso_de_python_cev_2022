# Exercício 83. Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão está com os parênteses abertos e fechados na ordem correta.

expressao = str(input("Digite uma expressão matemática: "))
cont = 0
for c in expressao:
    print(c)
    if c == ")":
        cont += 1
    if c == "(":
        cont -= 1
if cont == 0:
    print("expressão válida!")
else:
    print("Expressão inválida!")

# solução professor:

expr = str(input("Digite uma expressão: "))
pilha = []
for simb in expr:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("sua expressão está válida")
else:
    print("Sua expressão está errada")