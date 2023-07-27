# Exercício 104. Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: leiaInt("Digite um n")

def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print("\33[1;35mErro. Tente novamente!\33[m")
    return n


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")