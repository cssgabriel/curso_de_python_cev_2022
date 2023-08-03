<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$n = $read->read_int("Qual número você quer fatorar? ");

function fatorial($n, $show = false) {
  $f = 1;
  for ($i = $n; $i > 0; $i--) {
    $f *= $i;
    if ($show) {
      if ($i === 1) echo "{$i} = {$f}\n";
      else echo "{$i} x ";
    }
  }
  echo "Fatorial de {$n} é igual a {$f}!";
}

fatorial($n, true);