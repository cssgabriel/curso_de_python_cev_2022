<?php

require_once("z-line.php");
require_once("z-Read.php");

$read = new Read();
$numbers = [];
$n = 0;

while ($n !== 9999) {
  array_push($numbers, $n);
  $n = $read->read_int("Digite um número [9999 para sair]: ");
}

$count = count($numbers) - 1;
$sum = array_sum($numbers);

echo line();
echo "Você digitou {$count} números. A soma é de {$sum}.\n";
echo line();






