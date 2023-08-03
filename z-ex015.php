<?php

$km = (float) readline("Digite quantos Km foi rodado: ");
$dias = intval(readline("Digite quantos dias você ficou com o carro: "));
$amountToPay = ($km * 60) + ($dias * 0.15);
echo "O valor total a pagar é de R$ {$amountToPay}.";
