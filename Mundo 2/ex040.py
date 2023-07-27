# Exercício 40. Crie um programa que leia duas notas de um aluno e calcule sua média.
# Mostre uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
if media < 5:
    print("Sua média foi de {:.2F}. \33[1;31mREPROVADO".format(media))
elif media >= 5 and media <= 6.9:
    print("Sua média foi de {:.2F}. \33[1;33mRECUPERAÇÃO".format(media))
else:
    print("Sua média foi de {:.2F}. \33[1;32mAPROVADO".format(media))