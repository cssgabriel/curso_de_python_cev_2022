<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$matriz = [[],[],[]];

foreach (range(0, 2) as $i) {
  foreach (range(0, 2) as $z) {
    $n = $read->read_int();
    array_push($matriz[$i], $n);
  }
}
echo line();
foreach ($matriz as $line) {
  foreach ($line as $v) {
    $v = str_pad($v, 2, "0", STR_PAD_LEFT);
    echo "| {$v} |";
  }
  echo "\n";
}
echo line();

# A) A soma de todos os valores pares digitados.
$sum = array_sum(array_filter(array_reduce($matriz, fn($acc, $arr) => [...$acc,...$arr], []), fn($n) => $n % 2 === 0));
echo "A soma de todos os valores pares: {$sum}.\n";
echo line();

# B) A soma dos valores da terceira coluna.
echo "A soma dos valores da terceira coluna: ";
$sum = 0;
foreach ($matriz as $i => $row) {
  foreach ($row as $z => $col) {
    if ($z !== 2) continue;
    else {
      $sum += $col;
    }
  }
}
echo "{$sum}\n";
echo line();

# C) O maior valor da segunda linha.
echo "O maior valor da segunda linha: " . max($matriz[1]);
