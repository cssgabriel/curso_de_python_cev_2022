<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();

contador(0, 10, 1);
echo line();
contador(10, 0, 2);
echo textBox("Personalize sua contagem");

$inicio = $read->read_int("Início: ");
$fim = $read->read_int("Fim: ");
$passo = $read->read_int("Passo: ");
echo line();
contador($inicio,$fim,$passo);

function contador($inicio, $fim, $passo) {
  if ($inicio < $fim) {
    for($i = $inicio; $i <= $fim; $i += $passo) {
      sleep(1);
      echo "{$i}\n";
    }
  } else {
    for($i = $inicio; $i >= $fim; $i -= $passo) {
      echo "{$i}\n";
    }
  }
}

echo "FIM";