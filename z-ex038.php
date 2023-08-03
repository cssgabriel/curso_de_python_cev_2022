<?php

$n1 = (int) readline("Digite um número: ");
$n2 = (int) readline("Digite outro número: ");
if ($n1 > $n2) echo "O primeiro valor é MAIOR";
else if ($n2 > $n1) echo "O segundo valor é MAIOR";
else echo "Não existe valor maior, os dois são iguais";
