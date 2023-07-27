# Exercício 41. A Confederação Nacional de Natação precisa de um programa que leia o ano de nescimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
from datetime import date

ano = int(input("Digite o ano em que nasceu: "))
idade = date.today().year - ano
if idade <= 9:
    print("Você possui {} anos. Sua classificação é \33[1;34mMIRIM".format(idade))
elif idade <= 14:
    print("Você possui {} anos. Sua classificação é \33[1;34mINFANTIL".format(idade))
elif idade <= 19:
    print("Você possui {} anos. Sua classificação é \33[1;34mJUNIOR".format(idade))
elif idade <= 25:
    print("Você possui {} anos. Sua classificação é \33[1;34mSÊNIOR".format(idade))
else:
    print("Você possui {} anos. Sua classificação é \33[1;34mMASTER".format(idade))