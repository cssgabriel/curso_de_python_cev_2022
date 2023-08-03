<?php

require_once("z-line.php");
require_once("z-Read.php");
//require_once("z-Numbers.php");

$read = new Read();

$name = $read->read_str("Nome: ");
$average = $read->read_float("Média: ");
$students = ["name" => $name, "average" => $average];

switch ($average) {
  case $average < 5:
    $students["situation"] = "reprovado";
    break;
  case $average < 7:
    $students["situation"] = "recuperação";
    break;
  case $average >= 7:
    $students["situation"] = "aprovado";
    break;
  default:
    echo "Nota inválida.";
    break;
}

echo line();
foreach ($students as $k => $v) {
  echo "- {$k}: {$v}\n";
}