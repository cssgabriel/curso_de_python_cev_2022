# Exercício 62. Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar 0 termos.

termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))
cont = 1
enesimo = 10
resposta = 1
ac = 0
while resposta != 0:
    if resposta != 0:
        while cont <= enesimo:
            print("{} -> ".format(termo), end="")
            termo += razao
            cont += 1
            ac += 1
        print("FIM!")
    resposta = int(input(("\nQuer mostrar mais termos? Digite quantos: ")))
    enesimo = resposta
    cont = 1
print("-=" * 10)
print("Foram mostrados {} termos. Programa finalizado!".format(ac))
print("-=" * 10)
