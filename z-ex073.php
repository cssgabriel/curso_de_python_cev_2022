<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$times = [
  "Palmeiras","Corinthians","Athletico-PR","Atlético-MG",
  "Internacional","Fluminense","Botafogo","Santos","São Paulo",
  "Bragantino","Avaí","Atlético-GO","Ceará SC","Flamengo",
  "Coritiba","América-MG","Goiás","Cuiabá","Fortaleza","Juventude"
];

echo line();
echo "Os cinco primeiros colocados são: \n";
for ($i = 1; $i <= 5; $i++) {
  echo "{$i}º: {$times[$i]}\n";
}

echo line();
echo "Os quatro últimos colocados são: \n";
for ($i = count($times) - 1; $i > count($times) - 5; $i--) {
  echo "{$i}º: {$times[$i]}\n";
}

echo line();
echo "A lista em ordem alfabética é :\n";
sort($times);
foreach ($times as $time) {
  echo "{$time}\n";
}

echo line();
$k = array_search("Cuiabá", $times);
echo "Cuiabá está na {$k}ª posição.\n";
