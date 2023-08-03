<?php

require_once("z-line.php");
require_once("z-Read.php");
require_once("z-Numbers.php");

$read = new Read();
$numbers = new Numbers();

echo "Para encerrar o programa digite um valor negativo. Ex: -1."

while(true) {
  $n = $read->read_int("Quer ver a tabuada de qual valor? ");
  echo line();

  if ($n < 0) break;
  for ($i = 1; $i <= 10; $i++) {
    echo "{$i} x {$n} = " . $i * $n . PHP_EOL;
  }
  echo line();
}

echo "Programa finalizado. Volte sempre!";