def dobro(preco, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def aumenta(preco, porc, formato=False):
    res = preco + (preco * porc / 100)
    return res if not formato else moeda(res)


def diminui(preco, porc, formato=False):
    res = preco - (preco * porc / 100)
    return res if not formato else moeda(res)


def moeda(preco, moeda="R$"):
    return f"{moeda}{preco}".replace(".", ",")
