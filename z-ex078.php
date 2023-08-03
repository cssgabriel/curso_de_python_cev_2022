<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$numbers = [];

foreach (range(1, 5) as $i) {
  $n = $read->read_int("Digite um valor para adicionar na posição {$i}: ");
  $numbers[] = $n;
}

$maior = max($numbers);
$menor = min($numbers);
echo "Maior: {$maior}. Está na posição: " . array_search($maior, $numbers) + 1 . PHP_EOL;
echo "Menor: {$menor}. Está na posição: " . array_search($menor, $numbers) + 1 . PHP_EOL;