# Exercício 113. Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possbilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\33[1;31mPor favor, digite um número real válido.\33[m")
            continue
        except KeyboardInterrupt:
            print("\n\33[1;31mPrograma interrompido pelo usuário.\33[m")
            return 0
        else:
            return n


nint = leiaInt("Digite um valor: ")
nfloat = leiaFloat("Digite um valor: ")
print(f"O primeiro número que você digitou foi: {nint}")
print(f"O segundo número que você digitou foi: {nfloat}")
