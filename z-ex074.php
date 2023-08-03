<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$numbers = array_map(fn() => rand(0, 10), range(0, 4));
echo "Eu sorteei os números: \n";
foreach ($numbers as $n) {
  echo " -> {$n}";
}
echo "\n";
echo "O maior valor foi " . max($numbers) . PHP_EOL;
echo "O menor valor foi " . min($numbers);