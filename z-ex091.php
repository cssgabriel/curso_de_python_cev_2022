<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$ranking = [];

foreach (range(1, 4) as $i) {
  $n = rand(1, 6);
  $ranking["jogador {$i}"] = $n;
  echo "O Jogador {$i} tirou {$n} no dado.\n";
  sleep(1);
}
arsort($ranking);
echo line();
$c = 1;
foreach ($ranking as $k => $v) {
  echo "{$c}º lugar: {$k} com {$v}.\n";
  $c++;
}