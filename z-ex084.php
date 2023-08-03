<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();
$people = [];

while (true) {
  $name = $read->read_str("Nome: ");
  $weight = $read->read_float("Peso: ");
  array_push($people, array($name, $weight));
  $opt = $read->read_str("Quer continuar? [S/N] ", ["s", "n"]);
  if ($opt === "n") break;
}

$maior =  maiorPeso($people);
$menor =  menorPeso($people);
echo "Foram cadastradas " . count($people) . " pessoas.\n";
echo "O MAIOR peso registrado foi de {$maior[1]} Kg. Peso de {$maior[0]}.\n";
echo "O MENOR peso registrado foi de {$menor[1]} Kg. Peso de {$menor[0]}.\n";


function maiorPeso($arr) {
  $maior = ["", 0];
  foreach ($arr as $v) {
    if ($v[1] > $maior[1]) $maior = $v;
  }
  return $maior;
};

function menorPeso($arr) {
  $menor = ["", 0];
  foreach ($arr as $k => $v) {
    if ($k === 0) $menor = $v;
    if ($v[1] < $menor[1]) $menor = $v;
  }
  return $menor;
};
