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
    echo "| {$v} |";
  }
  echo "\n";
}
