# Exercício 112. Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from utilidades import dados, moeda

preco = dados.leiaDinheiro("Digite um valor: ")
moeda.resumo(preco, 15, 15)