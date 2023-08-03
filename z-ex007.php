<?php

$notas = [];
while(count($notas) < 2) {
    $notas[] = (float) readline("Digite um número: ");
}

$sum = array_reduce($notas, fn($acc, $n) => $acc + $n );
$media = $sum / count($notas);
echo "A média é: {$media}";

