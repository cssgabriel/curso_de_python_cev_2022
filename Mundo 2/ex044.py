# Exercício 44. Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% desconto
# - À vista cartão: 5% desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

valorProduto = float(input("Qual valor do produto? "))
opcao = int(input("""Qual a forma de pagamento? Escolha abaixo:
[ 1 ] DINHEIRO
[ 2 ] CHEQUE
[ 3 ] CARTÃO
Digite a opção desejada: """))
if opcao == 1 or opcao == 2:
    print("Você escolheu pagamento à vista por dinheiro ou cheque. Desconto de 10% aplicado.")
    print("De R$ {}, por R$ {}".format(valorProduto, valorProduto * 0.9))
elif opcao == 3:
    opcao = int(input("Você escolheu pagamento em cartão. Você vai dividir em quantas parcelas? "))
    if opcao == 1:
        print("Você escolheu pagar em {} parcela. Desconto de 5% aplicado.".format(opcao))
        total = valorProduto * 0.95
    elif opcao == 2:
        print("Você escolheu pagar em {} parcelas. Você pagará sem juros".format(opcao))
        total = valorProduto
    else:
        print("Você escolheu pagar em {} parcelas. Você pagará 20% de juros".format(opcao))
        total = valorProduto * 1.2
    print("De R$ {}, por R$ {}".format(valorProduto, total))
    print("{} parcelas de R$ {}".format(opcao, total / opcao))
else:
    print("Opção inválida. Digite novamente!")