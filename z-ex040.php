<?php

$n1 = (float) readline("Primeira nota: ");
$n2 = (float) readline("Segunda nota: ");

$m = ($n1 + $n2) / 2;

echo "Sua média é {$m}.\n";

if ($m < 5) echo "Média ABAIXO de 5.0: REPROVADO";
else if ($m <= 6.9 && 5 <= $m) echo "Média ENTRE 5.0 e 6.9: RECUPERAÇÃO";
else echo "Média 7.0 ou superior: APROVADO";
