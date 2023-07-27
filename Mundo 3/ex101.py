# Exercício 101. Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(n):
    from datetime import date
    ano = date.today().year
    idade = ano - n
    if idade >= 18:
        return f"Com {idade} anos, o voto é: Obrigatório"
    elif idade >= 16 or idade >= 65:
        return f"Com {idade} anos, o voto é: Opcional"
    else:
        return f"Com {idade} anos, o voto é: Negado"


nascimento = int(input("Em que ano você nasceu? "))
print(voto(nascimento))
