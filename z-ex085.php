<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
// $numbers = [];
$even = [];
$odd = [];

foreach (range(1, 7) as $i) {
  $n = $read->read_int();
  if ($n % 2 === 0) array_push($even, $n);
  else array_push($odd, $n);
}

sort($even);
sort($odd);

echo "Pares: " . implode(", ", $even) . PHP_EOL;
echo "Ímpares: " . implode(", ", $odd);
