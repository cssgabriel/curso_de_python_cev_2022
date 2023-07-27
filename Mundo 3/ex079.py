# Exercício 79. Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    valor = int(input("Adicione um valor: "))

    if valor in lista:
        print("Valor já existente. Não poderá ser adicionado!")
    else:
        lista.append(valor)
        print("Valor adicionado com sucesso!")

    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer adicionar outro valor? [S/N] ")).strip().upper()[0]
    if opcao == "N":
        break

lista.sort()
print(f"Os valores adicionados foram: {lista}")
