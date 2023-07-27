# Exercício 39. Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
ano = int(input("Em que ano você nasceu? "))
idade = datetime.date.today().year - ano
print("Você nasceu em {}, sua idade é de {} anos.".format(ano, idade))
if idade < 18:
    print("Ainda não chegou a hora de se alistar. Faltam {} ano(s).".format(18 - idade))
elif idade == 18:
    print("Cheogu a hora de se alistar!")
else:
    print("Já se passaram {} ano(s) para se alistar. Você deve ser alistar IMEDIATAMENTE!".format(idade - 18))