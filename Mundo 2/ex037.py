# Exercício 37. Escreva um programa que leia um número inteiro qualquer e pesa peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
import decimal

num = int(input("Digite um número inteiro: "))
escolha = int(input("""Qual conversão você quer realizar?
\33[1;33m[ 1 ] BINÁRIO
\33[1;34m[ 2 ] OCTAL
\33[1;31m[ 3 ] HEXADECIMAL\33[m
Digite sua escolha: """))
if escolha != 1 or escolha != 2 or escolha != 3:
    print("Digite uma opção válida: ")
if escolha == 1:
    print("O numéro {} convertido para \33[1;33mBINÁRIO\33[m vale {}!".format(num, bin(num)[2:]))
elif escolha == 2:
    print("O numéro {} convertido para \33[1;31mOCTAL\33[m vale {}!".format(num, oct(num)[2:]))
elif escolha == 3:
    print("O numéro {} convertido para \33[1;31mHEXADECIMAL\33[m vale {}!".format(num, hex(num)[2:]))
