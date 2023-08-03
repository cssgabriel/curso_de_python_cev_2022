<?php

$n = (int) readline("Digite um número: ");

$c = $n;
$fat = 1;
echo "Calculando {$n}! = ";
while ($c > 0) {
    echo "{$c}";
    echo $c > 1 ? " x " : " = ";
    $fat *= $c;
    $c--;
}

echo($fat);