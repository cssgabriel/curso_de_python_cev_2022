<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$numbers = [];

while (true) {
  $n = $read->read_int();
  array_push($numbers, $n);
  $opt = $read->read_str("Quer continuar? [S/N] ", ['s', 'n']);
  if ($opt === "n") break;
}

echo line();
echo "Foram digitados " . count($numbers) . " números.\n";
rsort($numbers);
echo "A lista em ordem descrescente é: " . implode(", ", $numbers) . PHP_EOL;

if (is_int(array_search(5, $numbers))) {
  $n5 = array_count_values($numbers)[5];
  if ($n5 > 1) {
    echo "O número 5 está nas posições: ";
    foreach ($numbers as $k => $v) {
      if ($v == 5) echo ", {$k}";
    }
    echo "\n";
  }
  else echo "O número 5 está na posição: {$n5}\n";
}
