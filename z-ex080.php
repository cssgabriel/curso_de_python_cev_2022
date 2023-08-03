<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$numbers = [];

foreach (range(0, 4) as $i) {
  $n = $read->read_int();
  
  if ($i === 0 || (isset($numbers[count($numbers) - 1]) && $n > $numbers[count($numbers) - 1])) array_push($numbers, $n);
  else {
    foreach ($numbers as $k => $v) {
      if ($n <= $v) {
        $numbers = array_merge(array_slice($numbers, 0, $k), array($n), array_slice($numbers, $k));
        echo "Adicionado na posição {$k} da lista\n";
        break;
      }
    }
  }
}

echo "Os valores digitados foram: " . implode(", ", $numbers);
