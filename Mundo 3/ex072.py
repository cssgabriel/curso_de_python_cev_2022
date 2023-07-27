# Exercício 72. Crie un programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

while True:
    n = int(input("Digite um valor entre 0 e 20: "))
    tupla = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove","dez", "onze", "doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")
    if 20 >= n >= 0:
        print("O valor digitador foi {}".format(tupla[n]))
    else:
        print("Tente novamente. ", end="")
    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
    if opcao == "N":
        break
print("Programa finalizado!")