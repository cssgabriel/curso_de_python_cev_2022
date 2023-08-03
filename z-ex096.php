<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();

function area(float | int $l, float | int $c) {
  return $l * $c;
}
$l = $read->read_float("Largura: ");
$c = $read->read_float("Comprimento: ");
echo "Área: " . area($l, $c) . "m².";