def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res


def aumenta(preco, porc):
    res = preco + (preco * porc / 100)
    return res


def diminui(preco, porc):
    res = preco - (preco * porc / 100)
    return res


def moeda(preco, moeda="R$"):
    return f"{moeda}{preco}".replace(".", ",")
