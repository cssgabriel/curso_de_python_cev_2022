<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$numeros = [];

function sorteio() {
  global $numeros;
  echo "Sorteando 5 valores: ";
  foreach (range(0,4) as $i) {
    $numeros[] = rand(0, 10);
  }
  echo implode(", ", $numeros) . PHP_EOL;
}

function somaPar() {
  global $numeros;
  $sum = 0;
  echo "Somando os valores pares de: " . implode(", ", $numeros);
  foreach ($numeros as $n) {
    if ($n % 2 === 0) $sum += $n;
  }
  echo " -> Temos: $sum";
}

sorteio($numeros);
print_r($numeros);
somaPar($numeros);