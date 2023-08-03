<?php

$valueOfHome = (float) readline("Qual o valor da casa? R$ ");
$salary = (float) readline("Qual o seu salário? R$ ");
$years = (int) readline("Quantos anos para quitar? ");

$installment = $valueOfHome / ($years * 12);
$limit = $salary * 30 / 100;

echo "Para comprar uma cada no valor de R$ {$valueOfHome} em {$years} anos, o valor da parcela deverá ser R$ " . number_format($installment, 2, ",", ".") . PHP_EOL;
echo "Calculando seu empréstimo...\n";
sleep(1);
echo "Seu empréstimo foi ";
echo $installment > $limit ? "NEGADO!" : "APROVADO!";
