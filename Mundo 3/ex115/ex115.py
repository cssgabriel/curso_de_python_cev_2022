# Exercício 115. Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar um nova pessoa e listar todas as pessoas cadastradas.

from lib import arquivo
from lib import interface

arq = "cursoemvideo.txt"
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"])
    if resposta == 1:
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        nome = str(input("Nome: "))
        idade = interface.leiaInt("Idade: ")
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        print("Saindo do sistema...")
        break
    else:
        print("Erro! Digite uma opção válida.")