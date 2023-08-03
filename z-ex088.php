<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$matriz = [[],[],[]];

echo line();
echo center("MEGA SENA");
echo line();

$n = $read->read_int("Quantos jogos você deseja? ");
foreach (range(1, $n) as $i) {
  sleep(1);
  $j = [];
  foreach (range(0, 5) as $z) {
    $j[] = str_pad(rand(0, 60), 2, "0", STR_PAD_LEFT);
  }
  echo "Jogo número {$i}: " . implode(", ", $j) . PHP_EOL;
}