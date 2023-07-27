# Exercício 102. Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, qu eserá um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    -> Calcula um fatorial de um número.
    :param n: Número que será calculado o fatorial
    :param show: (opcional) Este parâmetro quando em 'True' mostra a conta detalhada. Quando em 'False', mostra apenas o resultado
    :return: não possui
    """
    fac = 1
    for c in range(n, 0, -1):
        fac *= c
        if show == True:
            if c == 1:
                print(f"{c} = {fac}")
            else:
                print(f"{c} x ", end="")
    print(f"Fatorial de {n} é igual a {fac}!")


valor = int(input("Valor: "))
fatorial(valor, show=True)