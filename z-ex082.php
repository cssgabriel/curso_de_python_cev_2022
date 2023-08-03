<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$numbers = [];

while (true) {
  $n = $read->read_int();
  array_push($numbers, $n);

  $opt = $read->read_str("Quer continuar? [S/N] ", ["s", "n"]);
  if ($opt === "n") break;
}

$even = array_filter($numbers, fn($n) => $n % 2 === 0);
$odd = array_diff($numbers, $even);

echo "A lista gerada foi: " . implode(", ", $numbers) . PHP_EOL;
echo "Os números pares são: " . implode(", ", $even) . PHP_EOL;
echo "Os números ímpares são: " . implode(", ", $odd) . PHP_EOL;
