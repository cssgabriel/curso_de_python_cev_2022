<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();

function maior(...$numbers) {
  $maior = 0;
  foreach ($numbers as $n) {
    if ($n > $maior) $maior = $n;
  }
  return $maior;
}

echo maior(5,4,4,5,1,3,9) . PHP_EOL;
echo maior(6,0) . PHP_EOL;
echo maior(0) . PHP_EOL;
echo maior(9,1,2,3,5,4) . PHP_EOL;