# Exercício 105. Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação(opcional)
# Adicione também os docstrings.

def notas(*n, s=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos aunos.
    :param s: valor opcional, indicando se deve ou não adicionar situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    maior = menor = media = soma = cont = 0
    lista = list()
    turma = dict()
    lista.append(n)

    for c in lista:
        for k, v in enumerate(c):
            if k == 0 or v > maior:
                maior = v
            if k == 0 or v < menor:
                menor = v
            soma += v
            cont += 1

    turma["Total"] = cont
    turma["Maior"] = maior
    turma["Menor"] = menor
    media = soma / turma["Total"]
    turma["Media"] = media

    if s:
        if media >= 7:
            turma["Situação"] = "ÓTIMO"
        elif media >= 5:
            turma["Situação"] = "REGULAR"
        else:
            turma["Situação"] = "RUIM"

    return turma


# Adicionar solução professor.


print(notas(10, 8, 6, 4, s=True))
print(notas(6, 8, 6, 3, s=True))
print(notas(6, 8, 6, 5, 9, 10, s=True))
print(notas(4, 6, 1))