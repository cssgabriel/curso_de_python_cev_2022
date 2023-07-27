def leiaDinheiro(msg):
    while True:
        dinheiro = str(input(f"{msg}")).strip().replace(",", ".")
        if dinheiro.isalpha():
            print(f"\033[1;33mERRO: '{dinheiro}' é um dado inválido. Tente novamente!\033[m")
        else:
            break
    return float(dinheiro)