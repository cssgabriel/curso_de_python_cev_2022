def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\33[1;31mPor favor, digite um número inteiro válido.\33[m")
            continue
        except KeyboardInterrupt:
            print("\n\33[1;31mPrograma interrompido pelo usuário.\33[m")
            return 0
        else:
            return n


def linha(tam=30):
    return "_" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c += 1
    print(linha())
    opc = leiaInt("Sua opção: ")
    return opc