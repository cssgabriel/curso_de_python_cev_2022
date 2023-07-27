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
    return f"{moeda:<3}{preco:>7}".replace(".", ",")


def resumo(preco, a, d):
    print("-" * 30)
    print(f"{'RESUMO':^30}")
    print("-" * 30)
    print(f"{'Dobro':.<15}", end="")
    print(f"{dobro(preco, True):.>15}")
    print(f"{'Metade':.<15}", end="")
    print(f"{metade(preco, True):.>15}")
    print(f"{'Aumento':.<15}", end="")
    print(f"{aumenta(preco, a, True):.>15}")
    print(f"{'Decréscimo':.<15}", end="")
    print(f"{diminui(preco, d, True):.>15}")
